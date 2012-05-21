# PythonForiOSHacks - No jailbreak

Proof of concept for missing? iOS features using the [Python for iOS](http://itunes.apple.com/us/app/python-for-ios/id485729872?mt=8&ign-mpt=uo%3D4) app.

## Exmaples

### Telnet
	import urllib2
	exec(urllib2.urlopen('http://demian:4711/telnetserver.py').read())

### Webserver
	import urllib2
	exec(urllib2.urlopen('http://demian:4711/webserver.py').read())
	
## Contact
* [Twitter](https://twitter.com/#!/i_error)