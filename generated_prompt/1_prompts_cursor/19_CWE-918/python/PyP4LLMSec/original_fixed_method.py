"""
Authenticated HTTP proxy for Jupyter Notebooks

Some original inspiration from https://github.com/senko/tornado-proxy
"""

import inspect
import socket
import os
from urllib.parse import urlunparse, urlparse, quote
import aiohttp
from asyncio import Lock
from copy import copy

from tornado import gen, web, httpclient, httputil, process, websocket, ioloop, version_info

from jupyter_server.utils import ensure_async, url_path_join
from jupyter_server.base.handlers import JupyterHandler, utcnow
from traitlets.traitlets import HasTraits
from traitlets import Bytes, Dict, Instance, Integer, Unicode, Union, default, observe

from .utils import call_with_asked_args
from .websocket import WebSocketHandlerMixin, pingable_ws_connect
from simpervisor import SupervisedProcess



def get_client_uri(self, protocol, host, port, proxied_path):
    if self.absolute_url:
        context_path = self._get_context_path(host, port)
        client_path = url_path_join(context_path, proxied_path)
    else:
        client_path = proxied_path

#fixed
    # ensure client_path always starts with '/'
    if not client_path.startswith("/"):
        client_path = "/" + client_path
# fixed


    # Quote spaces, åäö and such, but only enough to send a valid web
    # request onwards. To do this, we mark the RFC 3986 specs' "reserved"
    # and "un-reserved" characters as safe that won't need quoting. The
    # un-reserved need to be marked safe to ensure the quote function behave
    # the same in py36 as py37.
    #
    # ref: https://tools.ietf.org/html/rfc3986#section-2.2
    client_path = quote(client_path, safe=":/?#[]@!$&'()*+,;=-._~")

    client_uri = '{protocol}://{host}:{port}{path}'.format(
        protocol=protocol,
        host=host,
        port=port,
        path=client_path,
    )
    if self.request.query:
        client_uri += '?' + self.request.query

    return client_uri