import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

_logger = logging.getLogger(__name__)

def render_ssh_key_preferences(self, panel_identifier, user_action=None, **extra_args):  # @UnusedVariable
    # Handle action
    ssh_delete_form = DeleteSshForm()
    if user_action == "add" and ssh_add_form.is_submitted():
        self._add_key(user_action, ssh_add_form)
    elif user_action == 'delete' and ssh_delete_form.is_submitted():
        self._delete_key(user_action, DeleteSshForm())

    # Get SSH keys if file exists.
    view_params = {'form': ssh_add_form}
    try:
        view_params["sshkeys"] = [
            {
                'title': key.comment or (key.keytype + ' ' + key.key[:18]),
                'fingerprint': key.fingerprint
            }
            for key in self.app.currentuser.authorizedkeys
        ]
    except IOError:
        view_params["sshkeys"] = []
        flash(_("Failed to get SSH keys"), level='error')
        _logger.warning("error reading SSH keys", exc_info=1)

    return "prefs_sshkeys.html", view_params
