#!/usr/bin/env python

"""
.. module:: fastagi
   :synopsis: FastAGI service for Asterisk

Requires modified pyst2 to support reading stdin/out/err

 Copyright 2011 VOICE1, LLC
 By: Ben Davis <ben@voice1-dot-me>

Specification
-------------
"""

import socketserver
import sys

import asterisk.agi

__verison__ = 0.1

# TODO: Read options from config file.
HOST, PORT = "127.0.0.1", 4573


class FastAGI(socketserver.StreamRequestHandler):
    # Close connections not finished in 5seconds.
    timeout = 5

    def handle(self):
        try:
            agi = asterisk.agi.AGI(stdin=self.rfile, stdout=self.wfile, stderr=sys.stderr)
            agi.verbose("pyst2: FastAGI on: {}:{}".format(HOST, PORT))
        except TypeError as e:
            sys.stderr.write(
                'Unable to connect to agi://{} {}\n'.format(self.client_address[0], str(e))
            )
        except socketserver.socket.timeout:
            sys.stderr.write('Timeout receiving data from {}\n'.format(self.client_address))
        except socketserver.socket.error:
            sys.stderr.write(
                'Could not open the socket. Is something else listening on this port?\n'
            )
        except Exception as e:
            sys.stderr.write('An unknown error: {}\n'.format(str(e)))


if __name__ == "__main__":
    # server = socketserver.TCPServer((HOST, PORT), FastAGI)
    server = socketserver.ForkingTCPServer((HOST, PORT), FastAGI)

    # Keep server running until CTRL-C is pressed.
    server.serve_forever()
