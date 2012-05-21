# PythonForiOSHacks - No jailbreak

Proof of concept for missing? iOS features using the [Python for iOS](http://itunes.apple.com/us/app/python-for-ios/id485729872?mt=8&ign-mpt=uo%3D4) app.

## Prerequisite
 * [Python for iOS](http://itunes.apple.com/us/app/python-for-ios/id485729872?mt=8&ign-mpt=uo%3D4)

## Examples

Enter the following examples into the Python for iOS shell.
Please review the fetched scripts if you don't trust me. Just some simple lines of python code…. ;)

* http://pastebin.com/raw.php?i=HTjPFEZN
* http://pastebin.com/raw.php?i=0J1HJ7M4


### Telnetserver

#### Start
	
	import urllib2
	exec(urllib2.urlopen('http://pastebin.com/raw.php?i=HTjPFEZN').read())
	
#### Connect to your iOS device
	telnet 192.168.100.115 4711
	Trying 192.168.100.115...
	Connected to ****-iphone.
	Escape character is '^]'.
	You connected from 192.168.100.200:52774
	ls /
	.Trashes
	.file
	Applications
	Developer
	Library
	System
	bin
	cores
	dev
	etc
	private
	sbin
	tmp
	usr
	var


	whoami
	mobile


	date
	2012-05-21 22:13:54


### Webserver

#### Start

	import urllib2
	exec(urllib2.urlopen('http://pastebin.com/raw.php?i=0J1HJ7M4').read())
	
#### Browse your iOS device
	http://iphoneiplan:4711/
	
## Contact
* [Twitter](https://twitter.com/#!/i_error)