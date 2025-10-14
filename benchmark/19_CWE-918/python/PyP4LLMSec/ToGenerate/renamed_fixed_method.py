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

    # Quote spaces, åäö and such, but only enough to send a valid web
    # request onwards. To do this, we mark the RFC 3986 specs' "reserved"
    # and "un-reserved" characters as safe that won't need quoting. The
    # un-reserved need to be marked safe to ensure the quote function behaves
    # the same in py36 as py37.
    #
    # ref: https://tools.ietf.org/html/rfc3986#section-2.2
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
