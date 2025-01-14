History
=======

2019-08-08  Francesco Rana <https://github.com/c1cc10>

    * Fixed send_command to work with python3 (by evilscientress )
    * changed 'async' option name in manager.py due to the updated
      reserved words list in Python 3

2016-11-04  VoiPCS <https://github.com/VoIPCS>

    * Fixing unicode bug in `send_action` for AMI.

2016-02-16  Randall Degges <https://github.com/rdegges>

    * Fixing issue in AGI class init function. Thanks to @sancho2934489 for the
      find!

2015-11-16  Scinawa Antani <https://github.com/Scinawa>

    * Fixing indentation errors.

2015-11-14  Ben Davis <https://github.com/tuxpowered>

    * Handling more UTF-8 encoding issues in `_quote` method.

2015-07-18  Artem Sorokin

    * Fixing UTF-8 encoding issues.

2015-07-15  Artem Sorokin

    * Fix multiline command end marker for OpenVox GSM Gateway.

2015-03-31  Randall Degges

    * Porting packaging to setuptools (modern).
    * Adding six as a dependency (it was missing before).

2015-03-30  Areski Belaid

    * Fixing the MANIFEST.in file I accidentally broke :)

2015-03-29  Timur Tuchkovenko <eill@yandex.ru>
    * UPGRADE: AMI fix for Python 3 compatibility.

2014-10-08  Timur Tuchkovenko <eill@yandex.ru>
    * UPGRADE: initial Python 3 support. Now pyst2 requires
      Python 'six' module. Some minor changes in other files.

2014-09-14  Sp1tF1r3 <https://github.com/Sp1tF1r3>
    * asterisk/manager.py: added action 'Reload' for Asterisk Manager
      Interface (AMI).

2013-12-03  Ludovic Gasc <gmludo@gmail.com>
    * examples/agi_script.py: added example script to explain AGI
      functionality.
    * README: renamed to REAMDE.rst for Github's Markdown support.
    * setup.py: minor changes.

2012-11-12  Arezqui Belaid <areski@gmail.com>
    * asterisk/manager.py: minor empty line enhancements.
    * examples/show_channels.py: added example script to show information via
      Asterisk Manager Interface (AMI).

2012-11-11  Arezqui Belaid <areski@gmail.com>
    * PEP8 Fixes

2011-05-31  Randall Degges <rdegges@gmail.com>
    * BUGFIX: Fixing issue that prevented manager.status command from returning
      proper output.

2007-01-26  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/manager.py: Make get_header() functions work like
      dict.get().
    * UPGRADE: Updated.

2007-01-16  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/manager.py: Fix support for Manager.command(). Patch from
      Karl Putland <karl@klasstek.com>.

2007-01-02  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/agi.py (AGI.set_autohangup): Fixed syntax error.

2006-11-28  Matthew Nicholson  <mnicholson@digium.com>

    * UPGRADE: Tweaked formatting.

2006-10-30  Matthew Nicholson  <mnicholson@digium.com>

    * ChangeLog: Fixed previous entry.

2006-10-30  Matthew Nicholson  <mnicholson@digium.com>

    * TODO: Updated.
    * asterisk/agi.py (AGI.control_stream_file): Changed default skipms
      and quoted arguments.

2006-10-24  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/agi.py: Added get_variable_full command.

2006-10-18  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/agitb.py: Make error output default to sys.stderr instead
      of sys.stdout.

2006-09-19  Matthew Nicholson  <mnicholson@digium.com>

    * debian/control: Removed XS-Python-Versions header to make it default
      to all python versions.

2006-09-19  Matthew Nicholson  <mnicholson@digium.com>

    * setup.py: Updated version.

2006-09-19  Matthew Nicholson  <mnicholson@digium.com>

    * debian/rules: Changed to use pysupport.
    * debian/control: Changed to use pysupport and changed arch to all.

2006-09-19  Matthew Nicholson  <mnicholson@digium.com>

    * MANIFEST.in: Added NEWS to manifest.

2006-09-19  Matthew Nicholson  <mnicholson@digium.com>

    * debian/rules: Updated to reflect new python policy.
    * debian/control: Updated to reflect new python policy.
    * debian/changelog: Updated.

2006-08-23  Matthew Nicholson  <mnicholson@digium.com>

    * UPGRADE: Updated.

2006-08-23  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/manager.py (unregister_event): Added.

2006-08-23  Matthew Nicholson  <mnicholson@digium.com>

    * NEWS: Added.

2006-07-14  Matthew Nicholson  <mnicholson@digium.com>

    * asterisk/agi.py (wait_for_digit): Only catch ValueError, not all
      exceptions.

2006-07-14  Matthew Nicholson  <mnicholson@digium.com>

    * TODO: Updated.
    * asterisk/agi.py (set_variable): Documentation changes.
    * asterisk/agi.py (get_variable): Changed to return and empty string
      instead of throwing an exception when a channel variable is not set.
    * UPGRADE: Added.

2006-07-14  Matthew Nicholson  <mnicholson@digium.com>

    * ChangeLog: Added.
    * TODO: Added.
    * MANIFEST.in: Added ChangeLog and TODO.
