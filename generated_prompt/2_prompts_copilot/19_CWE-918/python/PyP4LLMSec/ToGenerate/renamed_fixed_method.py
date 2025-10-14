"""
Authenticated HTTP proxy for Jupyter Notebooks
Some original inspiration from https://github.com/senko/tornado-proxy
"""
from urllib.parse import urlunparse, urlparse, quote
from jupyter_server.utils import ensure_async, url_path_join
def build_proxied_url(self, scheme, destination_host, destination_port, destination_path):
    if self.absolute_url:
        base_path = self._get_context_path(destination_host, destination_port)
        combined_path = url_path_join(base_path, destination_path)
    else:
        combined_path = destination_path
    #

    if not combined_path:
        combined_path = '/'
#

    combined_path = quote(combined_path, safe=":/?#[]@!$&'()*+,;=-._~")
    final_url = '{protocol}://{host}:{port}{path}'.format(
        protocol=scheme,
        host=destination_host,
        port=destination_port,
        path=combined_path,
    )
    if self.request.query:
        final_url += '?' + self.request.query
    return final_url
