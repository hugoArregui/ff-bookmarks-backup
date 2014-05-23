#!/usr/bin/env python

import telnetlib, argparse

parser = argparse.ArgumentParser(description='Firefox bookmarks backup tool')
parser.add_argument('output', metavar='FILE', type=str)
parser.add_argument('--host', metavar='host', type=str, default="localhost", help="mozrep host")
parser.add_argument('--port', metavar='port', type=int, default=4242, help="mozrep port")
args = parser.parse_args()

host = args.host
port = args.port
backup_to = args.output

print("Connecting to mozrep at %s:%s" % (host, port))
t = telnetlib.Telnet(host, port=port)
t.write(b'Components.utils.import("resource://gre/modules/XPCOMUtils.jsm");')
t.write(b'XPCOMUtils.defineLazyModuleGetter(this, "PlacesBackups", "resource://gre/modules/PlacesBackups.jsm");')
t.write(('PlacesBackups.saveBookmarksToJSONFile("%s");' % backup_to).encode('ascii'))
t.write(b'repl.quit()')
print("Done")
