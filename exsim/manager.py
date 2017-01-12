#! /usr/bin/env python

import logging
import pickle
import struct

logging.basicConfig(level=logging.DEBUG)


class Manager(object):
    """Server manager."""

    def __init__(self, sock, addr):
        self._socket = sock
        self._address = addr
        self._server = None
        self._table = {}
        self._buffer = ""
        return

    def set_server(self, server):
        self._server = server
        return

    def socket(self):
        return self._socket

    def close(self):
        self._socket.close()
        self._address = None
        return

    def readable(self):
        data = self._socket.recv(8192)
        if len(data) == 0:
            self._server.manager_closed(self)
            return

        self._buffer += data

        msg = self.parse_message()
        if not msg:
            return

        self.dispatch(msg)
        return


    def parse_message(self):

        # Check we have a header.
        if len(self._buffer) < 4:
            logging.debug("Manager buffer < 4")
            return None

        # Unpack header, and sanity check.
        l = struct.unpack("<L", self._buffer[:4])[0]
        if l > 65535:
            logging.debug("Manager buffer > 64KB (%d)" % l)
            return None

        # Check we have the full packet.
        if len(self._buffer) < l + 4:
            logging.debug("Manager received message fragment")
            return None

        msg = pickle.loads(self._buffer[4:l+4])
        self._buffer = self._buffer[l+4:]

        return msg
    

    def dispatch(self, message):
        """Handle a decoded management session message."""

        handler = self._table.get(message["type"], None)
        if not handler:
            logging.warning("No handler for '%s' request" % message["type"])
            # FIXME: create error reply.
            return

        reply = {}
        handler(message, reply)

        # FIXME: send reply

        return


    def handle_create_engine(self, request, reply):
        self._server.create_engine(request.name)
        reply.result = True
        return
