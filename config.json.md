# config.json

This is the [config.json](config.json) file annotated:

    {
        // this is a custom configuration option for use inside custom
		// applications
        "debug": true,

        // despite being named "address" this is _only_ a port number
        // at the moment
        "address": 8080,

        // defines the username/pass for the default user
        "root_user": { "password": "admin" },

        // list of modules that contain applications to load (ensure
        // that these modules have the appropriate entry point in
        // their setup.py!!)
        "applications": [
            "pserver.example"
        ],

        // define your databases and their various locations/settings
        // you can have many databases, and these are referenced by the
        // first segment of the plone.server path
        //
        // by default, there
        "databases": [{
            "zodb": {
                "storage": "ZODB",
                "path": "var/Data.fs"
            }
        }]
    }


More config file related information:

  * [official documentation](http://ploneserver.readthedocs.io/en/latest/configuration.html)
  * [default example](https://github.com/plone/plone.server/blob/master/config.json) (basically the same as the ZODB example)
  * [NEWT example](https://github.com/plone/plone.server/blob/master/config-newt.json) (postgres jsonb)
  * [ZEO example](https://github.com/plone/plone.server/blob/master/config-zeo.json)
  * [ZODB example](https://github.com/plone/plone.server/blob/master/config-zodb.json)
