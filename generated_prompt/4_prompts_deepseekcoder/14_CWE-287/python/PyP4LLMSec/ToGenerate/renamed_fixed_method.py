from twisted.python import log
def validate_and_select_security(self, client_version):

    if client_version == self.VERSION:
        log.msg("Client version %s is valid" % client_version.strip())
        #
        self.selected_protocol = "VNC"
        self.selected_protocol_version = "RF
        B"
#
        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % client_version)
        self.transport.loseConnection()
