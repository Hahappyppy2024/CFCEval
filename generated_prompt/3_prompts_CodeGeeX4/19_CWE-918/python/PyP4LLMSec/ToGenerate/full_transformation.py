from urllib.parse import urlunparse, urlparse, quote
from jupyter_server.utils import ensure_async, url_path_join

def build_proxied_client_url(self, scheme, target_host, target_port, target_path):
    if not self.absolute_url:
        combined_path = target_path
    else:
        base_context_path = self._get_context_path(target_host, target_port)
        combined_path = url_path_join(base_context_path, target_path)
    #
    return combined_path
    #
    combined_path = quote(combined_path, safe=":/?#[]@!$&'()*+,;=-._~")
    proxied_url = '{protocol}://{host}:{port}{path}'.format(
        protocol=scheme,
        host=target_host,
        port=target_port,
        path=combined_path,
    )
    if self.request.query:
        proxied_url += '?' + self.request.query
    return proxied_url
