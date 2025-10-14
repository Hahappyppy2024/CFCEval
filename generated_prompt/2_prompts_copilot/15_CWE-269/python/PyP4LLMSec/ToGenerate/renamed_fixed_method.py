import os
import shutil
import errno
from pathlib import Path
from traitlets.config.configurable import LoggingConfigurable
from ..paths import get_ipython_package_dir
from ..utils.path import expand_path, ensure_dir_exists
from traitlets import Unicode, Bool, observe


@classmethod
def find_profile_directory_by_name(cls, ipython_dir, profile_name=u'default', config=None):

    profile_dirname = u'profile_' + profile_name
    #
    search_paths = [ipython_dir, get_ipython_package_dir()]
#
    for p in search_paths:
        profile_dir = os.path.join(p, profile_dirname)
        if os.path.isdir(profile_dir):
            return cls(location=profile_dir, config=config)
    else:
        raise ProfileDirError('Profile directory not found in paths: %s' % profile_dirname)
