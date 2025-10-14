from twisted.python import log
def check_version(self, version):
    """
    Determine the client's version and decide whether to continue the
    handshake.
    """
    if version == self.VERSION:
        log.msg("Client version %s is valid" % version.strip())

        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % version)
        self.transport.loseConnection()