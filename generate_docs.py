import importlib
import os
import re
import shutil
import sys

rootPath = 'docs_temp'
srcPath = 'src'
buildPath = 'build'
rstPath = os.path.join(rootPath, 'rst')
parsePath = os.path.join(rootPath, 'parse')


def indent(amount):
    return ' ' * 3 * amount


def generateHelpDoc(name):
    consoleOut = sys.stdout
    path = os.path.join(parsePath, name + '.txt')
    sys.stdout = open(path, 'w')
    help(name)
    sys.stdout = consoleOut


class ParsedModule(object):
    def __init__(self, name):
        self.name = name
        self.submodules = []
        self.classes = []
        importlib.import_module(name)
        generateHelpDoc(name)
        for submodule in self.getNames('SUBMODULES'):
            self.submodules.append(ParsedModule('{}.{}'.format(self.name, submodule)))
        for _class in self.getNames('CLASSES', ParsedClass.filterName):
            self.classes.append(ParsedClass('{}.{}'.format(self.name, _class)))

    def getNames(self, header, nameFilter=None):
        names = []
        with open(os.path.join(parsePath, self.name + '.txt')) as helpFile:
            # Find the start of list
            line = helpFile.readline()
            while line.strip() != header:
                line = helpFile.readline()
                if not line:
                    return []
            # Read through all of the names
            while line:
                line = helpFile.readline().strip()
                if line and (not nameFilter or nameFilter(line)):
                    names.append(line)
        return names

    def getClasses(self):
        classes = list([_class.name for _class in self.classes])
        for submodule in self.submodules:
            classes.extend(submodule.getClasses())
        return classes

    def write(self, classes):
        output = open(os.path.join(rstPath, self.name + '.rst'), 'w')
        output.write(".. _{}:\n\n".format(self.name))
        output.write(self.name)
        output.write("\n==================\n\n")
        for _class in self.classes:
            _class.write(output, classes)
        for submodule in self.submodules:
            submodule.write(classes)

    def writeTocEntry(self, tocFile):
        tocFile.write("   {}\n".format(self.name))
        for submodule in self.submodules:
            submodule.writeTocEntry(tocFile)

    def writeListEntry(self, tocFile):
        tocFile.write("* :ref:`{}`\n\n".format(self.name))
        for submodule in self.submodules:
            submodule.writeTocEntry(tocFile)


class ParsedClass(object):
    def __init__(self, modulename):
        self.name = modulename.split('.')[-1]
        self.modulename = modulename
        self.description = ''
        self.methods = []
        self.attributes = []
        self.data = []
        generateHelpDoc(modulename)
        parsers = [
            (ParsedMethod, self.methods),
            (ParsedStaticMethod, self.methods),
            (ParsedAttribute, self.attributes),
            (ParsedData, self.data)
        ]
        with open(os.path.join(parsePath, modulename + '.txt'), 'r') as parseFile:
            line = parseFile.readline()
            while line:
                for parser, container in parsers:
                    if parser.shouldParse(line):
                        parser.parse(parseFile, container)
                        break
                line = parseFile.readline()

    def write(self, output, classes):
        output.write(self.name)
        output.write("\n{}\n".format('-' * 35))
        output.write(".. class:: {}\n\n".format(self.name))
        output.write("{}{}\n\n".format(indent(1), self.description))
        for group in [self.methods, self.attributes, self.data]:
            for item in group:
                item.write(output, classes)

    @staticmethod
    def filterName(name):
        return not name.startswith("Boost.") and not 'map_index' in name and "(Boost.Python.instance)" not in name

    @staticmethod
    def addRef(name, classes):
        if name in classes:
            return ':class:`{}`'.format(name)
        return name

    @staticmethod
    def addRefs(text, classes):
        words = re.findall(r'\b\S+\b', text)
        for word in words:
            if word in classes:
                text = text.replace(word, ':class:`{}`'.format(word))
        return text


class ParsedMethod(object):
    def getMethodType(self):
        return 'method'

    def isStatic(self):
        return self.getMethodType() == 'staticmethod'

    @staticmethod
    def shouldParse(line):
        return "Methods defined here:" in line

    @staticmethod
    def parse(parseFile, container):
        ParsedMethod._parse(parseFile, container, ParsedMethod)

    @staticmethod
    def _parse(parseFile, container, MethodClass):
        line = parseFile.readline()
        methodName = ''
        parsed = None
        while line and '----------------' not in line:
            line = line[2:].lstrip()
            if '(...)' in line:
                #Start parsing a new method
                methodName = line[:line.index('(')]
            elif ' -> ' in line:
                if methodName != line[:line.index('(')]:
                    raise RuntimeError("Method name does not match previous method.")
                parsed = MethodClass()
                parsed.signature, parsed.args, parsed.returns = ParsedMethod.parseSignature(line, parsed.isStatic())
                parsed.description = ''
                for arg in parsed.args:
                    pass
                container.append(parsed)
            elif parsed:
                # Reading current parsed method docstring
                if line.startswith(':param'):
                    # Get dosctring for arg
                    line = line.split(' ', 1)[1]
                    name = line[:line.index(':')]
                    for arg in parsed.args:
                        if arg.name == name:
                            arg.docstring = line[line.index(' '):]
                            break
                elif line.startswith(':type'):
                    line = line.split(' ', 1)[1]
                    name = line[:line.index(':')]
                    for arg in parsed.args:
                        if arg.name == name:
                            arg.argType = line[line.index(' '):]
                            break
                elif line.startswith(':rtype: '):
                    parsed.returns = line[8:]
                else:
                    parsed.description += line
            line = parseFile.readline()

    @staticmethod
    def parseSignature(line, isStatic):
        args = []
        if '()' not in line:
            for arg in line.split(' ', 1)[1].split(','):
                argData = arg.lstrip().split(' ')[0][1:].split(')')
                argType = argData[0]
                try:
                    argData = argData[1].split('=')
                except IndexError:
                    print line
                    continue
                argName = argData[0]
                argDefault = argData[1] if len(argData) == 2 else None
                args.append(ParsedArg(argName, argType, argDefault))
        name = line.split('(', 1)[0]
        signature = name + '( '
        if args and not isStatic:
            del args[0]
        defaultCount = 0
        for index, arg in enumerate(args):
            if arg.default is not None:
                defaultCount += 1
                signature += '['
            if index != 0:
                signature += ', '
            signature += '{}'.format(arg.name)
            if arg.default is not None:
                signature += '=' + arg.default
            if index == len(args) - 1:
                signature += ']' * defaultCount
        signature += ')'
        returns = line.split()[-2] if line.endswith(':\n') else line.split()[-1]
        if returns == 'None':
            returns = ''
        return signature, args, returns

    def write(self, output, classes):
        output.write("{}.. {}:: {}\n\n".format(indent(1), self.getMethodType(), self.signature))
        output.write("{}{}\n\n".format(indent(2), ParsedClass.addRefs(self.description, classes)))
        for arg in self.args:
            if arg.docstring or arg.argType:
                output.write("{}:param {}: {}\n\n".format(indent(2), arg.name, ParsedClass.addRefs(arg.docstring, classes)))
            if arg.argType:
                output.write("{}:type {}: {}\n\n".format(indent(2), arg.name, ParsedClass.addRef(arg.argType, classes)))
        if self.returns:
            output.write("{}:rtype: {}\n\n".format(indent(2), ParsedClass.addRef(self.returns, classes)))


class ParsedStaticMethod(ParsedMethod):
    def getMethodType(self):
        return 'staticmethod'

    @staticmethod
    def shouldParse(line):
        return "Static methods defined here:" in line

    @staticmethod
    def parse(parseFile, container):
        ParsedMethod._parse(parseFile, container, ParsedStaticMethod)


class ParsedArg(object):
    def __init__(self, name, argType, default):
        self.name = name
        self.argType = argType
        self.default = default
        self.docstring = ''


class ParsedAttribute(object):
    @staticmethod
    def shouldParse(line):
        return "Data descriptors defined here:" in line

    @staticmethod
    def parse(parseFile, container):
        line = parseFile.readline()
        while line and '----------------' not in line:
            if len(line) > 5:
                parsed = ParsedAttribute()
                parsed.name = line[4:].strip()
                parsed.docstring = ''
                line = parseFile.readline()
                while line and line.startswith(" |      "):
                    parsed.docstring += line
                    line = parseFile.readline()
                container.append(parsed)
            else:
                line = parseFile.readline()

    def write(self, output, classes):
        output.write("{}.. attribute:: {}\n\n".format(indent(1), self.name))
        output.write("{}{}\n\n".format(indent(2), ParsedClass.addRefs(self.docstring, classes)))


class ParsedData(object):
    @staticmethod
    def shouldParse(line):
        return "Data and other attributes defined here:" in line

    @staticmethod
    def parse(parseFile, container):
        line = parseFile.readline()
        while line and '----------------' not in line:
            if ' = ' in line and '<built-in' not in line:
                parsed = ParsedData()
                parsed.data = line[4:].strip()
                # TODO: Blacklisted list
                if '__instance_size__' not in parsed.data:
                    container.append(parsed)
            line = parseFile.readline()

    def write(self, output, classes):
        output.write("{}.. data:: {}\n\n".format(indent(1), self.data))


def writeToc(rootModule):
    indexFile = open(os.path.join(rstPath, 'index.rst'), 'w')
    indexFile.write("\nWelcome to Crea's documentation!\n")
    indexFile.write("================================\n\n")
    indexFile.write("Contents:\n\n")
    indexFile.write(".. toctree::\n")
    indexFile.write("   :maxdepth: 2\n\n")
    rootModule.writeTocEntry(indexFile)
    indexFile.write("Welcome to the world of Crea!")
    indexFile.write("\n...\n\n")
    indexFile.write("Indices and tables\n")
    indexFile.write("==================\n\n")
    indexFile.write("* :ref:`genindex`\n")
    indexFile.write("* :ref:`modindex`\n")
    indexFile.write("* :ref:`search`\n")
    indexFile.close()


def main():
    if os.path.exists(rootPath):
        shutil.rmtree(rootPath)
    os.makedirs(rootPath)
    os.makedirs(parsePath)
    os.makedirs(rstPath)
    siegeModule = ParsedModule('siege')
    classes = siegeModule.getClasses()
    siegeModule.write(classes)
    writeToc(siegeModule)
    for f in os.listdir(rstPath):
        shutil.copyfile(os.path.join(rstPath, f), os.path.join(srcPath, f))
    shutil.rmtree(rootPath)
    os.system('sphinx-build -b html {src} {dst}'.format(src=srcPath, dst=buildPath))


if __name__ == '__main__':
    main()
