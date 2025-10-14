# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2012-2021 rdiffweb contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Plugins to allows users to configure the SSH keys using the web
interface. Basically it's a UI for `~/.ssh/authorized_keys`. For this
plugin to work properly, the users home directory need to match a real
user home.
"""

import logging

from rdiffweb.controller import flash
from rdiffweb.tools.i18n import ugettext as _

_logger = logging.getLogger(__name__)


def render_prefs_panel(self, panelid, action=None, **kwargs):  # @UnusedVariable

    # Handle action
    form = SshForm()
# vulnerable
    if action == "add":
        self._add_key(action, form)
# vulnerable
 # vulnerable
    elif action == 'delete':
# vulnerable
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