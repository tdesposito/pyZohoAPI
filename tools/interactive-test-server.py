# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import sys
sys.path.insert(0, "..")

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from os import system
from pprint import pprint
import signal
import traceback
import urllib

from pyzohoapi import *
from pyzohoapi.exceptions import ZohoException
from private import testdata

hostName = "localhost"
serverPort = 8080

params = {
    'orgid': testdata['orgid'],
	'refresh_token': testdata['api']['refresh_token'],
	'client_id': testdata['api']['client_id'],
	'client_secret': testdata['api']['client_secret'],
}
blank_params = {
    'api': 'inventory',
    'type': "",
    'id': "",
    'xtrapath': "",
    'qparams': "",
    'results': {},
    'apiinfo': {},
}

apiobjs = {
    'books': ZohoBooks(testdata['orgid'], "US", **testdata['api']),
    'inventory': ZohoInventory(testdata['orgid'], "US", **testdata['api']),
}

class RequestHandler(BaseHTTPRequestHandler):
    def sendFile(self, ext, type):
        with open(__file__.replace(".py", f".{ext}"), "r") as f:
            contents = f.read()
        self.send_response(200)
        self.send_header("Content-type", f"text/{type}")
        self.end_headers()
        self.wfile.write(bytes(contents, "utf-8"))

    def sendTemplate(self):
        with open(__file__.replace(".py", ".html"), "r") as f:
            template = f.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(template.format(**params), "utf-8"))

    def do_GET(self):
        if self.command == "GET":
            params.update(blank_params)
        if self.path == "/":
            self.sendTemplate()
        elif self.path == "/favicon.ico":
            self.send_response(404)
            self.end_headers()
        elif self.path == "/local.js":
            self.sendFile("js", "javascript")
        elif self.path == "/local.css":
            self.sendFile("css", "css")

    def do_POST(self):
        rawform = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        form = { k:v for k,v in [e.split("=") for e in rawform.split("&")] if v }
        for k in ['qparams', 'xtrapath']:
            if k in form:
                form[k] = urllib.parse.unquote_plus(form[k])
        params.update(form)
        api = apiobjs.get(form['api'])
        if form['action'] == "get":
            frag = f"{form['type']}{'/' + form['id'] if form.get('id') else ''}{'/' + form['xtrapath'] if form.get('xtrapath') else ''}"
            try:
                rsp = api.get(frag, params['qparams'])
                params['results'] = json.dumps(rsp)
                params['apiinfo'] = json.dumps({k:str(v) for k,v in api._ratelimit.items()})
            except ZohoException as e:
                params['results'] = json.dumps({
                    'Exception': {
                        'class': e.__class__.__name__,
                        'message': str(e),
                        'traceback': [l for l in traceback.format_exc().split('\n')]
                    }
                })

        return self.do_GET()

if __name__ == "__main__":
    server = ThreadingHTTPServer((hostName, serverPort), RequestHandler)
    server.daemon_threads = True
    server.allow_reuse_address = True
    def signal_handler(signal, frame):
        print("Exiting due to keyboard interrupt...")
        try:
            if (server):
                server.server_close()
        finally:
            sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    print(f"Server started http://{hostName}:{serverPort}")
    print("Press Ctrl-C to exit.")
    system("title pyZohoAPI Testing Server")

    system(f"start http://{hostName}:{serverPort}")
    try:
        while True:
            sys.stdout.flush()
            server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
