=========
Changelog
=========

.. note::
    Due to this library relying on external content, older versions are not guaranteed to work.
    Try to always use the latest version.

.. _v2.4.1:
2.4.1 (2019-11-20)
==================
- Fixed incorrect argument name (house) in ``Character`` constructor.

.. _v2.4.0:
2.4.0 (2019-11-20)
==================
- Added support for multiple houses per character. Accessible on ``Character.houses`` field.
- ``Character.house`` is now deprecated. It will contain the character's first house or ``None``.

.. _v2.3.4:
2.3.4 (2019-11-14)
==================
- Fixed bug with deaths not being parsed when a killer had ``and`` in their name.

.. _v2.3.3:

2.3.3 (2019-11-04)
==================
- Fixed bug with world parsing when there are more than 1000 players online.

.. _v2.3.2:

2.3.2 (2019-10-17)
==================
- Fixed incorrect highscores URL.

.. _v2.3.1:

2.3.1 (2019-10-06)
==================
- Fixed a bug with deaths not being parsed when a killer in assists had ``and`` in their name.

.. _v2.3.0:

2.3.0 (2019-09-16)
==================
- Added proxy option to client.

.. _v2.2.6:

2.2.6 (2019-09-01)
==================
- Fixed bug with account badges parsing failing when no badges were selected.

.. _v2.2.5:

2.2.5 (2019-08-22)
==================

- Fixed account badges parsing due to changes on the layout by CipSoft.

.. _v2.2.4:

2.2.4 (2019-08-20)
==================

- Disabled client compression for POST requests.

.. _v2.2.3:

2.2.3 (2019-08-17)
==================

- Enabled client side compression

.. _v2.2.2:

2.2.2 (2019-08-17)
==================

- Fixed killed by players and players kill stats being inverted for ``KillStatistics``

.. _v2.2.1:

2.2.1 (2019-08-10)
==================

- Fixed bug with character parsing failing when the guild rank is ``(member)``.

.. _v2.2.0:

2.2.0 (2019-08-08)
==================

- Added support for account badges and character titles.

.. _v2.1.0:

2.1.0 (2019-06-17)
==================

- Added ways to sort and filter House list results like in Tibia.com.
- Added support to get the Boosted Creature of the day.

.. _v2.0.1:

2.0.1 (2019-06-04)
==================

- Replaced references to ``secure.tibia.com`` with ``www.tibia.com`` as the former always redirects to the front page.

.. _v2.0.0:

2.0.0 (2019-06-03)
==================

- Added asynchronous client to fetch and parse Tibia.com sections.
- Added news parsing.
- Added kill statistics parsing.
- Added support for tournament worlds.
- Added support for house prices with 'k' suffixes.

.. _v1.1.3:

1.1.3 (2019-01-29)
==================

- Fixed incorrect parsing of deaths with summons involved when parsing characters from TibiaData.

.. _v1.1.2:

1.1.2 (2019-01-22)
==================

- Fixed TibiaData URLs of tibia characters with special characters in their names. (e.g Himmelhüpferin)

.. _v1.1.1:

1.1.1 (2019-01-09)
==================

- Fixed character houses having attributes mixed up.

.. _v1.1.0:

1.1.0 (2019-01-09)
==================

- Parsing Highscores from Tibia.com and TibiaData.
- Some strings from TibiaData had unpredictable trailing whitespaces,
  all leading and trailing whitespaces are removed.
- Added type hints to many variables and methods.

.. _v1.0.0:

1.0.0 (2018-12-23)
==================

-  Added support for TibiaData JSON parsing. To have interoperability
   between Tibia.com and TibiaData.
-  Added support for parsing Houses, House lists, World and World list
-  Added support for many missing attributes in Character and Guilds.
-  All objects are now serializable to JSON strings.

.. _v0.1.0:

0.1.0 (2018-08-17)
==================

Initial release:

-  Parses content from tibia.com

   -  Character pages
   -  Guild pages
   -  Guild list pages

-  Parses content into JSON format strings.
-  Parses content into Python objects.
