A Python wrapper for the MOC (Music on Console) audio player that
simplifies programmatic control and removes the complexity of
command-line flag management. This library provides a clean interface
for controlling audio playback during focused listening sessions,
enabling distraction-free music exploration and content discovery.

The core philosophy emphasizes **reducing friction in interactive audio
consumption** by handling MOC server lifecycle, audio system
dependencies (like JACK on macOS), and error recovery automatically.
Rather than memorizing MOC command syntax and managing server states
manually, this wrapper enables seamless audio navigation, timestamp
jumping, and playlist management for deep listening experiences.

**Who benefits from this library:** - Music enthusiasts who want precise
control over audio playback during active listening - Podcast listeners
who need to mark and revisit specific moments - Audio content reviewers
requiring frame-accurate navigation - Musicians and audio learners
analyzing recordings in detail - Python developers building simple audio
control interfaces - Anyone wanting distraction-free, keyboard-driven
audio control

Install
-------

Install the actual `MOC player/server <https://moc.daper.net/>`__

::

   sudo apt-get install -y moc

or

::

   brew install moc

Then install this package with ``pip``

::

   pip install mocp

Optional Installs redis-helper and yt-helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If redis-helper and yt-helper are installed, the FILES collection will
be updated with the basename of the the current playing file whenever
``moc.info_string()`` is called.

Install with ``pip``

::

   pip install "yt-helper[redis-helper]"

or

::

   pip install "mocp[extras]"

QuickStart
----------

.. code:: python

   import moc

   # Discover and play audio files from directories
   moc.find_and_play('~/Music', '~/Podcasts')  # Plays all audio files found

   # Interactive file selection for focused listening
   moc.find_select_and_play('~/Music')  # Shows menu to choose specific files

   # Precise navigation during active listening
   moc.toggle_pause()        # Play/pause current audio
   moc.seek(30)             # Seek forward 30 seconds
   moc.go('1h23m45s')       # Jump to specific timestamp for bookmarked moments
   moc.volume_up(10)        # Quick volume adjustments

   # Monitor current playback for context awareness
   info = moc.get_info_dict()
   print(moc.info_string())  # Shows: "2:15 (135) of 4:30 into song.mp3"

   # Discover content for listening sessions
   audio_files = moc.find_audio('~/Music/**/*.mp3', '~/Downloads')
   print(f"Found {len(audio_files)} audio files")

**What you gain:** Eliminate manual MOC server management and
command-line complexity during focused listening. The library handles
audio system setup, server lifecycle, and provides intelligent file
discovery, letting you concentrate on the music rather than technical
details. Perfect for building seamless, distraction-free audio
experiences.

API Overview
------------

Interactive Audio Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Smart Content Discovery and Playback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``find_and_play(*paths)``** - Discover and automatically play all
   audio files from specified locations

   -  ``*paths``: Filename and dirname globs (files or directories
      containing audio files)
   -  Returns: None (starts playback of discovered files)
   -  Internal calls: ``find_audio()``, ``start_server()``,
      ``bh.run_output()``

-  **``find_select_and_play(*paths)``** - Interactive audio file
   selection for curated listening sessions

   -  ``*paths``: Filename and dirname globs
   -  Returns: None (shows selection menu, then plays chosen files)
   -  Internal calls: ``find_audio()``, ``ih.make_selections()``,
      ``start_server()``, ``bh.run_output()``

-  **``find_audio(*paths)``** - Discover audio files matching path
   patterns for content exploration

   -  ``*paths``: Glob patterns for files or directories (supports ~
      expansion and recursive directory walking)
   -  Returns: List of quoted audio file paths ready for MOC playback
   -  Internal calls: None

Server and System Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transparent Server Control
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``start_server(n=1, max_calls=3)``** - Start MOC server with
   automatic audio system handling

   -  ``n``: Current attempt number for recursive retry logic
   -  ``max_calls``: Maximum retry attempts before giving up
   -  Returns: None (server started or error messages printed)
   -  Internal calls: ``bh.run_output()``, ``_start_jack()``,
      ``rm_pid_and_kill_jack()``

-  **``stop_server()``** - Clean shutdown of MOC server and audio
   dependencies

   -  Returns: None (stops server and cleans up JACK processes on macOS)
   -  Internal calls: ``bh.run_output()``, ``rm_pid_and_kill_jack()``

Playback Context Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``get_info_dict()``** - Retrieve current player state and file
   metadata for context awareness

   -  Returns: Dict with keys like ‘file’, ‘currenttime’, ‘currentsec’,
      ‘totaltime’, ‘state’
   -  Internal calls: ``bh.run_output()``

-  **``info_string(template='{currenttime} ({currentsec}) of {totaltime} into {file}')``**
   - Format current playback status for display

   -  ``template``: String template for custom formatting of player
      state
   -  Returns: Formatted string or empty string if stopped/error
   -  Internal calls: ``ih.get_string_maker()``, ``get_info_dict()``,
      ``add_current_to_FILES()``

Focused Listening Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~

Core Transport Functions
^^^^^^^^^^^^^^^^^^^^^^^^

-  **``toggle_pause()``** - Toggle between play and pause states during
   active listening

   -  Returns: None (changes playback state, auto-starts server if
      needed)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``next()``** - Skip to next track in current listening session

   -  Returns: None (advances playlist position)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``previous()``** - Skip to previous track in current listening
   session

   -  Returns: None (moves to previous playlist position)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``stop()``** - Stop current playback while preserving session
   context

   -  Returns: None (stops audio playback)
   -  Internal calls: ``bh.run_output()``

Precise Navigation for Content Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``seek(n)``** - Relative seeking for quick content exploration

   -  ``n``: Number of seconds (positive=forward, negative=backward)
   -  Returns: None (updates playback position)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``go(timestamp)``** - Jump to absolute position for bookmarked
   moments and precise navigation

   -  ``timestamp``: Target time in formats like ‘3h4m5s’, ‘2h15s’,
      ‘47m’, ‘300s’, ‘3:04:05’, ‘2:00:15’, ‘47:00’, ‘300’
   -  Returns: None (seeks to position, resumes playback if paused,
      handles segfault fallback)
   -  Internal calls: ``ih.timestamp_to_seconds()``,
      ``get_info_dict()``, ``toggle_pause()``, ``bh.run_output()``,
      ``start_server()``, ``seek()``

Immediate Audio Adjustments
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``volume_up(n=5)``** - Quick volume increase during listening

   -  ``n``: Volume increment (default 5)
   -  Returns: None (increases audio volume)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``volume_down(n=5)``** - Quick volume decrease during listening

   -  ``n``: Volume decrement (default 5)
   -  Returns: None (decreases audio volume)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

-  **``volume(n)``** - Set specific volume level for optimal listening
   experience

   -  ``n``: Target volume level
   -  Returns: None (sets volume to specific level)
   -  Internal calls: ``bh.run_output()``, ``start_server()``

Session Enhancement (Optional yt-helper Integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Listening History and Bookmarks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **``add_current_to_FILES()``** - Track currently playing file for
   session continuity and favorite marking

   -  Requires yt-helper and redis-helper packages
   -  Returns: None (adds/updates file metadata in persistent storage
      for cross-session access)
   -  Internal calls: ``get_info_dict()``, ``FILES.add()``,
      ``FILES.get_hash_id_for_unique_value()``, ``FILES.update()``

Getting the C source
--------------------

   MOC is written is written in C and hosted in an SVN repo (not Git).
   See ``man git-svn``

::

   $ git svn clone svn://svn.daper.net/moc/trunk moc
