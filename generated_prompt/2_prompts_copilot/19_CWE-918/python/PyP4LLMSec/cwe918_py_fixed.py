# FROM PyP4LLMSection: CWE-918

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

