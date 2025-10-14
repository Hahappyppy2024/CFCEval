import logging

from rdiffweb.controller import flash
from rdiffweb.tools.i18n import ugettext as _

ssh_logger = logging.getLogger(__name__)


def render_ssh_config_panel(self, panel_identifier, user_action=None, **extra_params):
    ssh_form = SshForm()
    if user_action == "add":
        self._add_key(user_action, ssh_form)
    elif user_action == 'delete':
        self._delete_key(user_action, DeleteSshForm())

    view_context = {'form': ssh_form}
    try:
        view_context["sshkeys"] = [
            {
                'title': key.comment or (key.keytype + ' ' + key.key[:18]),
                'fingerprint': key.fingerprint
            }
            for key in self.app.currentuser.authorizedkeys
        ]
    except IOError:
        view_context["sshkeys"] = []
        flash(_("Failed to get SSH keys"), level='error')
        ssh_logger.warning("error reading SSH keys", exc_info=1)

    return "prefs_sshkeys.html", view_context
