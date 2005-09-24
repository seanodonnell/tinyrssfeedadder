#!/usr/bin/env python

app="tinyrssfeedadder"
name="Tiny RSS Feed Adder"
description="A easy way to add feeds to your tiny rss installation"
author="Sean O'Donnell"
authorURL="http://blog.odonnell.nu"
uid='0a2ae0-4a29-4a42-aef2-dc50c5e555dc'

major_version = 0
minor_version = 0
build_version = 0
in_development = True

version = "%d.%d.%d%s" % (
	major_version,
	minor_version,
	build_version,
	indevelopment and "+" or ""

)

homepageURL="http://blog.odonnell.nu/%(app)s" % vars()
updateURL = %(homepageURL)s/update.rdf" % vars()
updateFile = "%(app)s-%(version)s.xpi" % vars()
updateLink = "%(homepageURL)s/%(updateFile)s" % vars()
firefoxUID = '6a172e3-922a-45ba-b36c-9387f798309b'
firefoxMinVersion = '1.0.7'
firefoxMaxVersion = '1.0.7'

overlays = (
	# overlay this on that

	('%(app)s/content/browser.xul' % vars(), 'browser/content/browser.xul' % vars()),
)

stylesheets = (
	#overlay this on that
)

skins = {
	'classic':{
		'skin_version':'1.0',
		'display_name': name,
	},
}

locales = {
	'en-US' : {
		'locale_version' : '1.0',
		'display_name' : 'English (US)',
		},
	},
}
