import os
import shutil
import errno
from pathlib import Path
from traitlets.config.configurable import LoggingConfigurable
from ..paths import get_ipython_package_dir
from ..utils.path import expand_path, ensure_dir_exists
from traitlets import Unicode, Bool, observe
@classmethod
def find_profile_dir_by_name(cls, ipython_dir, name=u'default', config=None):

    dirname = u'profile_' + name
    #
    paths = [
        os.path.expanduser(u'~/.ipython/profile_default'),
        os.path.expanduser(u'~/.ipython/profile_ipython'),
        os.path.expanduser(u'~/.ipython/profile_default'),
    #

    for p in paths:
        profile_dir = os.path.join(p, dirname)
        if os.path.isdir(profile_dir):
            return cls(location=profile_dir, config=config)
    else:
        raise ProfileDirError('Profile directory not found in paths: %s' % dirname)