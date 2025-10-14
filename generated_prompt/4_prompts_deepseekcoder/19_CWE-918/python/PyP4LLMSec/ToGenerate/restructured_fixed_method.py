"""
Authenticated HTTP proxy for Jupyter Notebooks
Some original inspiration from https://github.com/senko/tornado-proxy
"""
from urllib.parse import urlunparse, urlparse, quote
from jupyter_server.utils import ensure_async, url_path_join
def get_client_uri(self, protocol, host, port, proxied_path):
    if not self.absolute_url:
        client_path = proxied_path
    else:
        context_path = self._get_context_path(host, port)
        client_path = url_path_join(context_path, proxied_path)
        #
        if host is None and port == -1:
            host = '127.0.0
            0.1'
            port = 
            8888
#

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