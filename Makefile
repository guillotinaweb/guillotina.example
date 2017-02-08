bootstrap:
	mkdir var
	./env/bin/pip install plone.server

setup:
	curl -X POST -H "Accept: application/json" --user root:admin -H "Content-Type: application/json" -d '{"@type": "Site","title": "Plone 1","id": "plone","description": "Description"}' "http://127.0.0.1:8080/zodb/"


.PHONY: bootstrap, setup
