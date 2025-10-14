from twisted.python import log
def check_version(self, version):

    valid_version_msg_template = "Client version %s is valid"
    if version == self.VERSION:
        log.msg(valid_version_msg_template % version.strip())
        #
        self.select_security_type = self.SECURITY_TYPE_NONE
        # Return the security type and a status code indicating success
#
        return self.select_security_type, 1
    else:
        log.err("Can't handle VNC version %r" % version)
        self.transport.loseConnection()