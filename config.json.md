# config.json

This is the [config.json](config.json) file annotated:

    {
        // this is a custom configuration option for use inside custom
        // applications
        "debug": true,

        // interace:port service will be hosted on
        "host": "0.0.0.0",
        "port": 8080,

        // defines the username/pass for the default user
        "root_user": { "password": "admin" },

        // list of modules that contain applications to load (ensure
        // that these modules have the appropriate entry point in
        // their setup.py!!)
        "applications": [
            "example"
        ],

        // define your databases and their various locations/settings
        // you can have many databases, and these are referenced by the
        // first segment of the guillotina path
        //
        // note: ZODB is not supported any longer since it's not truly async
        "databases": [{
            "db": {
                "storage": "postgresql",
                "type": "postgres",
                "dsn": {
                    "scheme": "postgres",
                    "dbname": "postgres",
                    "user": "postgres",
                    "host": "db",
                    "password": "postgres",
                    "port": 5432
                },
                "options": {
                    "read_only": false
                }
            }
        }],

        // these are classes that have an 'extract_token' method -- the intent
        // of which is to examine a request and parse out information for use
        // by a particular auth policy
        "auth_extractors": [
            // pulls out AUTHORIZATION header and passes the value as the token
            "guillotina.auth.extractors.BearerAuthPolicy",

            // pulls out AUtHORIZATION header, decodes it, and splits it into a userid and token
            "guillotina.auth.extractors.BasicAuthPolicy",

            // pulls ws_token from querystring, decrypts it and passes the claimed token back
            "guillotina.auth.extractors.WSTokenAuthPolicy"
        ],

        // these are classes that have a 'get_user' method that takes the user
        // token and returns a user object if the user is found
        "auth_user_identifiers": [],

        // these are classes that, basically, have a "validate" method which
        // takes extracted data for a particular auth policy type and validates
        // the token against 
        "auth_token_validators": [
            // validates basic auth passwords
            "guillotina.auth.validators.SaltedHashPasswordValidator",

            // validates JWT tokens
            "guillotina.auth.validators.JWTValidator"
        ],

        // CORS related configuration
        // for an article that might help explain what CORS is and does, see:
        //
        //  https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
        //
        "cors": {
            "allow_origin": ["http://localhost:8080"],
            "allow_methods": ["GET", "POST", "DELETE", "HEAD", "PATCH", "OPTIONS"],
            "allow_headers": ["*"],
            "expose_headers": ["*"],
            "allow_credentials": true,
            "max_age": 3660
        },

        // JSON Web Token configuration
        // Reading RFC7519 might help explain what JWT is and does:
        //
        //  https://tools.ietf.org/html/rfc7519
        //
        "jwt": {
            "secret": "foobar",
            "algorithm": "HS256"
        }

    }


More config file related information:

  * [official documentation](http://guillotina.readthedocs.io/en/latest/installation/configuration.html)
  * [default example](https://github.com/plone/guillotina/blob/master/guillotina/cookiecutter/configuration/file.tmpl)
