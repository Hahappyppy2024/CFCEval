import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

ssh_logger = logging.getLogger(__name__)

def render_ssh_keys_view(self, panel_identifier, user_action=None, **extra_args):  # @UnusedVariable
    ssh_add_form = SshForm()
    #
    ssh_delete_form = DeleteSshForm()
    if user_action == 'add' and ssh_add_form.is_submitted():
#
        self._add_key(user_action, ssh_add_form)
    elif user_action == 'delete' and ssh_delete_form.is_submitted():
        self._delete_key(user_action, DeleteSshForm())
    ssh_view_data = {'form': ssh_add_form}
    try:
        ssh_view_data["sshkeys"] = [
            {
                'title': key.comment or (key.keytype + ' ' + key.key[:18]),
                'fingerprint': key.fingerprint
            }
            for key in self.app.currentuser.authorizedkeys
        ]
    except IOError:
        ssh_view_data["sshkeys"] = []
        flash(_("Failed to get SSH keys"), level='error')
        ssh_logger.warning("error reading SSH keys", exc_info=1)
    return "prefs_sshkeys.html", ssh_view_data
