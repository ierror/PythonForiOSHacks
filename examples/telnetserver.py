#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import shutil
import urllib2
from tempfile import mkdtemp
from zipfile import ZipFile


zip_name = 'telnetserver.zip'

try:
    # download and extract telnet server zip

    ## crate tmp download dir
    tmpdir = mkdtemp()
    os.chdir(tmpdir)
    with open(zip_name, 'wb+') as zip_fh:
        ## download to created tmp dir
        zip_fh.write(
                urllib2.urlopen('http://miniboa.googlecode.com/files/miniboa-r42.zip').read()
        )

    ## extract telnet server zip and chg into extracted dir
    ZipFile(zip_name).extractall()
    telnet_lib_dir = '%s/miniboa-r42/' % (tmpdir)
    os.chdir(telnet_lib_dir)
    sys.path.insert(0, telnet_lib_dir)

    ## start telnet server on port 4711
    CLIENTS = []
    def on_connect(client):
        CLIENTS.append(client)
        client.send('You connected from %s\r\n' % client.addrport())

    def on_disconnect(client):
        CLIENTS.remove(client)

    from miniboa import TelnetServer
    server = TelnetServer(port=4711)
    server.on_connect = on_connect
    server.on_disconnect = on_disconnect
    print 'Waiting on port 4711 for connections...'
    while True:
        for client in CLIENTS:
            if client.cmd_ready:
                cmd = client.get_command()

                # ls
                if cmd.startswith('ls'):
                    client.send(
                        '\n'.join(
                            os.listdir(
                                cmd.split(' ')[1] if len(cmd.split(' ')) > 1 else '/'
                            )
                        )
                    )

                # date
                elif cmd.startswith('date'):
                    from time import gmtime, strftime
                    client.send(strftime('%Y-%m-%d %H:%M:%S', gmtime()))

                # whoami
                elif cmd.startswith('whoami'):
                    import pwd
                    client.send(pwd.getpwuid(os.getuid())[0])

                client.send('\n')
                client.cmd_ready = False
        server.poll()

finally:
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)
