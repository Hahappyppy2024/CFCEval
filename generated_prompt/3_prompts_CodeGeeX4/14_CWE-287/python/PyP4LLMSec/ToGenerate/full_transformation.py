from twisted.python import log

def validate_and_select_security(self, client_version):

    valid_version_msg_template = "Client version %s is valid"
    if client_version == self.VERSION:
        log.msg(valid_version_msg_template % client_version.strip())
        #
        if self.select_security_type == 1:
            #
            return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % client_version)
        self.transport.loseConnection()
