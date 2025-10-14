from twisted.python import log
def validate_and_select_security(self, client_version):

    if client_version == self.VERSION:
        log.msg("Client version %s is valid" % client_version.strip())
        #
        self.select_security_type = self.SECURITY_TYPE_NONE
        # Return the security type and a status code indicating success
#
        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % client_version)
        self.transport.loseConnection()
