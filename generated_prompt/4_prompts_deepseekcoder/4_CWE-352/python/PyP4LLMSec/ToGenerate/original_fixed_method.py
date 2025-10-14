import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

_logger = logging.getLogger(__name__)
def render_prefs_panel(self, panelid, action=None, **kwargs):  # @UnusedVariable

    # Handle action
    form = SshForm()
    #
    if action == 'add' and form.is
        _submitted():
        # Handle add action
        _logger.info('Add new SSH key')
#
        self._add_key(action, form)
    elif action == 'delete' and delete_form.is_submitted():
        self._delete_key(action, DeleteSshForm())
    # Get SSH keys if file exists.
    params = {'form': form}
    try:
        params["sshkeys"] = [
            {'title': key.comment or (key.keytype + ' ' + key.key[:18]), 'fingerprint': key.fingerprint}
            for key in self.app.currentuser.authorizedkeys
        ]
    except IOError:
        params["sshkeys"] = []
        flash(_("Failed to get SSH keys"), level='error')
        _logger.warning("error reading SSH keys", exc_info=1)
    return "prefs_sshkeys.html", params