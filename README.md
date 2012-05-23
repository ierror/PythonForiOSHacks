# PythonForiOSHacks - No jailbreak

Proof of concept for missing? iOS features using the [Python for iOS](http://itunes.apple.com/us/app/python-for-ios/id485729872?mt=8&ign-mpt=uo%3D4) app.

## Prerequisite
 * [Python for iOS](http://itunes.apple.com/us/app/python-for-ios/id485729872?mt=8&ign-mpt=uo%3D4)

## Examples

Enter the following examples into the Python for iOS shell.
Please review the fetched scripts if you don't trust me. Just some simple lines of python code…. ;)

* Telnetserver: http://pastebin.com/HTjPFEZN
* Webserver: http://pastebin.com/0J1HJ7M4


### Telnetserver

#### Start
	
	import urllib2
	exec(urllib2.urlopen('http://pastebin.com/raw.php?i=HTjPFEZN').read())
	
#### Connect to your iOS device
	telnet <current IP address of your iOS device> 4711
	
#### Type one of implemented commands
* ls /
* whoami
* date

### Webserver

#### Start

	import urllib2
	exec(urllib2.urlopen('http://pastebin.com/raw.php?i=0J1HJ7M4').read())
	
#### Browse your iOS device
	http://<current IP address of your iOS device>:4711/
	
## Contact
* [Twitter](https://twitter.com/#!/i_error)