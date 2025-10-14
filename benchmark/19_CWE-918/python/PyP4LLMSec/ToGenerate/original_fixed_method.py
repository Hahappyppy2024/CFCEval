"""
Authenticated HTTP proxy for Jupyter Notebooks
Some original inspiration from https://github.com/senko/tornado-proxy
"""
from urllib.parse import urlunparse, urlparse, quote
from jupyter_server.utils import ensure_async, url_path_join

def get_client_uri(self, protocol, host, port, proxied_path):
    if self.absolute_url:
        context_path = self._get_context_path(host, port)
        client_path = url_path_join(context_path, proxied_path)
    else:
        client_path = proxied_path

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