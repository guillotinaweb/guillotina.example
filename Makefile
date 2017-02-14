# This make file assumes that you have a virtualenv at the location `./env`

bootstrap:
	# directory used for data.fs and related files in this example
	mkdir var
	# install dependencies
	./env/bin/pip install -r requirements.txt
	# make sure to install your app into your environment ;)
	./env/bin/python setup.py develop

setup:
	# create your initial site in the selected database
	curl -X POST -H "Accept: application/json" --user root:admin -H "Content-Type: application/json" -d '{"@type": "Site","title": "Plone 1","id": "plone","description": "Description"}' "http://127.0.0.1:8080/zodb/"

create_custom_type:
	# create an object of type CustomType and store it at the root
	curl -X POST -H "Accept: application/json" --user root:admin -H "Content-Type: application/json" -d '{"@type":"CustomType","title":"Custom Type 1","id":"customtype1","pserver.example.behaviors.ICustomBehavior":{"bar":"changed"}}' "http://127.0.0.1:8080/zodb/plone/"

modify_custom_behavior_content:
	# this will change the data in the custom behavior for the object created
	# with the `create_custom_type` target
	curl -X PATCH -H "Accept: application/json" --user root:admin -H "Content-Type: application/json" -d '{"pserver.example.behaviors.ICustomBehavior":{"bar":"changed"}}' "http://127.0.0.1:8080/zodb/plone/customtype1"

.PHONY: bootstrap setup createcustomtype
