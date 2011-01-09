This file is for you to describe the battleplan application. Typically
you would include information such as the information below:

Requirements
============
This application has a couple of requirements.

The most prominent being that it has to have access to a eve database dump.

The solution I used to create this was my own program,
http://github.com/udoprog/evedb

There is a dump available at http://toolchain.eu/open/eve.sql.gz

This will only create the databases necessary for the solarsystem,
constellations and regions, you will still have to setup-app in order to get
battleplan working.

Example
=======
For an example deployment, go to http://toolchain.eu/bp/
Api login has been disabled, allowing you to login by providing any
information at the 'signin' screen.

Installation and Setup
======================

Install ``battleplan`` using easy_install::

    easy_install battleplan

Make a config file as follows::

    paster make-config battleplan config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.
