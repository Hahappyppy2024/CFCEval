from twisted.python import log
def check_version(self, version):

    if version == self.VERSION:
        log.msg("Client version %s is valid" % version.strip())
        #
        if self.select_security_type == 1:
#
        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % version)
        self.transport.loseConnection()