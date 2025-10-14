from twisted.python import log

def validate_and_select_security(self, client_version):
    """
    Determine the client's version and decide whether to continue the
    handshake.
    """

    if client_version == self.VERSION:
        log.msg("Client version %s is valid" % client_version.strip())
        # Hardcoded: 1 security type: VNC Auth.
        self.transport.write("\x01\x02")
        # fixed
        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % client_version)
        self.transport.loseConnection()
