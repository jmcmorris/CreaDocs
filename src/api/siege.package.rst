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

      

      :param packagePath: 

      :type packagePath: object

   .. method:: discoverContent( )

      

   .. method:: get( content)

      

      :param content: 

      :type content: str

      :rtype: :class:`Content`

   .. method:: get( contentId)

      

      :param contentId: 

      :type contentId: int

      :rtype: :class:`Content`

   .. method:: getContents( )

      

      :rtype: :class:`ContentIdMap`

   .. method:: getPackages( )

      

      :rtype: :class:`PackageList`

   .. method:: loadContent( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :rtype: :class:`Content`

   .. method:: pack( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: packContent( content, stream)

      

      :param content: 

      :type content: :class:`Content`

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: populateContentEntities( entityManager)

      

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: read( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: unpack( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: unpackContent( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :rtype: :class:`Content`

   .. method:: validate( )

      

      :rtype: bool

   .. method:: write( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: writeContent( content, stream)

      

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

      

      :rtype: :class:`ContentMap`

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: isEnabled( )

      

      :rtype: bool

   .. method:: read( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. method:: validate( )

      

      :rtype: bool

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: getAuthor

      

   .. attribute:: getDescription

      

   .. attribute:: getName

      

   .. attribute:: path

      

   .. attribute:: priority

      

   .. attribute:: title

      

   .. attribute:: version

      

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

      

      :param arg2: 

      :type arg2: object

   .. method:: getOrdered( [coreLoading=siege.package.CorePackageLoading.First])

      

      :param coreLoading: 

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

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. method:: setPriority( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Package`

      :param arg3: 

      :type arg3: int

   .. method:: validate( )

      

      :rtype: bool

   .. method:: write( arg2)

      

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

