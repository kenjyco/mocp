Install
-------

Install the actual `MOC player/server <https://moc.daper.net/>`__

::

   % sudo apt-get install -y moc

   or

   % brew install moc

Then install this package with ``pip``

::

   % pip3 install mocp

Optional Installs
-----------------

redis-helper and yt-helper
~~~~~~~~~~~~~~~~~~~~~~~~~~

If redis-helper and yt-helper are installed, the FILES collection will
be updated with the basename of the the current playing file whenever
``moc.info_string()`` is called

Install with ``pip``

::

   % pip3 install "yt-helper[redis-helper]"

   or

   % pip3 install "mocp[extras]"

Usage
-----

.. code:: python

   In [1]: import moc

   In [2]: moc.find_and_play('~/music-dir/blah*')

   In [3]: moc.go('12:15')         # jump to particular point in current track

   In [4]: moc.go('1h23m12s')      # jump to particular point in current track

   In [5]: moc.go(500)             # jump to particular point in current track

   In [6]: moc.info_string()
   Out[6]: '08:21 (501) of 95:35 into /home/user/music-dir/blah-thing/file.mp3'

Getting the C source
--------------------

   MOC is written is written in C and hosted in an SVN repo (not Git).
   See ``man git-svn``

::

   $ git svn clone svn://svn.daper.net/moc/trunk moc
