.. _siege.package:

siege.package
==================

CorePackageLoading
-----------------------------------
.. class:: CorePackageLoading

   

   .. data:: First = siege.package.CorePackageLoading.First

   .. data:: Last = siege.package.CorePackageLoading.Last

   .. data:: None = siege.package.CorePackageLoading.None

Content
-----------------------------------
.. class:: Content

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Content`

      :rtype: object

   .. method:: __init__( id, package, path)

      

      :param id: 

      :type id: int

      :param package: 

      :type package: str

      :param path: 

      :type path: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: getEntity( )

      

      :rtype: :class:`Entity`

   .. method:: getId( )

      

      :rtype: int

   .. method:: getName( )

      

      :rtype: str

   .. method:: getPackage( )

      

      :rtype: str

   .. method:: getPath( )

      

      :rtype: str

   .. staticmethod:: nameFromPath( path)

      :return: filename without extension.


      :param path: 

      :type path: object

      :rtype: str

   .. attribute:: entity

      

   .. attribute:: id

      

ContentIdMap
-----------------------------------
.. class:: ContentIdMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

ContentMap
-----------------------------------
.. class:: ContentMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

ContentStash
-----------------------------------
.. class:: ContentStash

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: discover( packagePath)

      Uses this ContentStash's :class:`PackageList` instance to discover all packages in the given path.


      :param packagePath: 

      :type packagePath: object

   .. method:: discoverContent( )

      Discovers all contents in this stash and adds it to the internal list.


   .. method:: get( content)

      Searches for :class:`Content` by name and optional package name.


      :param content:  either content path or "<package>:<path>".


      :type content: str

      :rtype: :class:`Content`

   .. method:: get( contentId)

      Searches for :class:`Content` by id.


      :param contentId: 

      :type contentId: int

      :rtype: :class:`Content`

   .. method:: getContents( )

      

      :rtype: :class:`ContentIdMap`

   .. method:: getPackages( )

      

      :rtype: :class:`PackageList`

   .. method:: loadContent( stream)

      Currently, calls unpackContent.


      :param stream: 

      :type stream: :class:`DataStream`

      :rtype: :class:`Content`

   .. method:: pack( stream)

      see `siege.package.PackageList.write`


      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: packContent( content, stream)

      Writes content id to :class:`DataStream`.


      :param content: 

      :type content: :class:`Content`

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: populateContentEntities( entityManager)

      Creates :class:`Content` entities using the passed :class:`EntityManager`.


      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: read( stream)

      (Re)Initialises this :class:`ContentStash` via `siege.package.PackageList.read` and also discovers all packages in "mods"


      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: unpack( stream)

      (Re)Initialises this :class:`ContentStash` via `siege.package.PackageList.read`


      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: unpackContent( stream)

      Reads content id from :class:`DataStream`.


      :param stream: 

      :type stream: :class:`DataStream`

      :rtype: :class:`Content`

   .. method:: validate( )

      see `siege.package.PackageList.validate`


      :rtype: bool

   .. method:: write( stream)

      Writes max content id to :class:`DataStream` and calls see `siege.package.PackageList.write`


      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: writeContent( content, stream)

      Currently, calls packContent.


      :param content: 

      :type content: :class:`Content`

      :param stream: 

      :type stream: :class:`DataStream`

Package
-----------------------------------
.. class:: Package

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`Content`

   .. method:: getContents( )

      (map) The contents this module contains.


      :rtype: :class:`ContentMap`

   .. method:: has( arg2)

      :return: true if this package contains the specified content.


      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: isEnabled( )

      

      :rtype: bool

   .. method:: read( arg2)

      Reads the package attributes, content ids and content paths from the passed :class:`DataStream`.


      :param arg2: 

      :type arg2: :class:`DataStream`

   .. method:: validate( )

      Validates whether package path & referenced content files exist.


      :rtype: bool

   .. method:: write( arg2)

      Writes this package's attributes, content ids and content paths to the passed :class:`DataStream`.


      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: getAuthor

       |      The python module's "author" attribute.


   .. attribute:: getDescription

       |      The python module's "description" attribute.


   .. attribute:: getName

      

   .. attribute:: path

       |      Path to the python module.


   .. attribute:: priority

       |      If set, the priority at which this module should be loaded.


   .. attribute:: title

       |      The python module's "title" attribute.


   .. attribute:: version

       |      The python module's "version" attribute.


PackageList
-----------------------------------
.. class:: PackageList

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: disablePackage( arg2)

      

      :param arg2: 

      :type arg2: :class:`Package`

   .. method:: discover( arg2)

      Discovers all packages in the passed Path.


      :param arg2: 

      :type arg2: object

   .. method:: getOrdered( [coreLoading=siege.package.CorePackageLoading.First])

      Returns an ordered list of packages.


      :param coreLoading:  (optional), order in which to list the core package.


      :type coreLoading: :class:`CorePackageLoading`

      :rtype: :class:`Packages`

   .. method:: getPackage( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`Package`

   .. method:: hasPackage( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: read( arg2)

      see `siege.package.Package.read`


      :param arg2: 

      :type arg2: :class:`DataStream`

   .. method:: setPriority( arg2, arg3)

      Sets order priority for a package.


      :param arg2: 

      :type arg2: :class:`Package`

      :param arg3: 

      :type arg3: int

   .. method:: validate( )

      see `siege.package.Package.validate`


      :rtype: bool

   .. method:: write( arg2)

      see `siege.package.Package.write`


      :param arg2: 

      :type arg2: :class:`DataStream`

PackageMap
-----------------------------------
.. class:: PackageMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

Packages
-----------------------------------
.. class:: Packages

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

