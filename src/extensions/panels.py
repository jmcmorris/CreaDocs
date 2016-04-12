# -*- coding: utf-8 -*-
"""
    This is a pretty hacky attempt to expose Panels. Needs to be cleaned up but mostly functional now.
"""

from docutils import nodes
from docutils.parsers.rst import directives

import sphinx
from sphinx.locale import _
from sphinx.environment import NoUri
from sphinx.util.nodes import set_source_info
from sphinx.util.compat import Directive


class panel_node(nodes.General, nodes.Element):
    pass


class Panel(Directive):
    """
    A panel entry
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        env = self.state.document.settings.env
        targetid = 'index-%s' % env.new_serialno('index')
        targetnode = nodes.target('', '', ids=[targetid])

        if not self.options.get('class'):
            self.options['class'] = ['panel-group']

        text = '\n'.join(self.content)
        panel = panel_node(text)
        title_text = self.content[0]
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        panel.title = title_text
        # panel += nodes.title(title_text, '', *textnodes)
        # panel += messages
        panel['classes'] += self.options['class']
        del self.content[0]
        self.state.nested_parse(self.content, self.content_offset + 1, panel)
        panel = [panel]

        set_source_info(self, panel[0])
        return [targetnode] + panel


def process_todos(app, doctree):
    # collect all todos in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'panel_all_panels'):
        env.panel_all_panels = []
    for node in doctree.traverse(panel_node):
        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.panel_all_panels.append({
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'todo': newnode,
            'target': targetnode,
        })



def purge_todos(app, env, docname):
    if not hasattr(env, 'panel_all_panels'):
        return
    env.panel_all_panels = [panel for panel in env.panel_all_panels if panel['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'panel_all_panels'):
        return
    if not hasattr(env, 'panel_all_panels'):
        env.panel_all_panels = []
    env.panel_all_panels.extend(other.panel_all_panels)


def visit_panel_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS="panel panel-primary panel-group"))
    self.body.append('<div class="panel-heading">')
    self.body.append('<h3 class="panel-title">{title}</h3>'.format(title=node.title))
    self.body.append('</div>')
    self.body.append('<div class="panel-body">')


def depart_panel_node(self, node):
    self.body.append('</div></div>')


def setup(app):
    app.add_config_value('panel_include_panels', False, 'html')

    app.add_node(panel_node, html=(visit_panel_node, depart_panel_node))

    app.add_directive('panel', Panel)
    app.connect('env-purge-doc', purge_todos)
    app.connect('env-merge-info', merge_info)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
