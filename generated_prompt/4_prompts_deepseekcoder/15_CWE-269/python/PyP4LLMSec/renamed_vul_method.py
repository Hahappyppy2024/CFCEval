import os

@classmethod
def find_profile_directory_by_name(cls, ipython_dir, profile_name=u'default', config=None):
    """Find an existing profile dir by profile name, return its ProfileDir.

    This searches through a sequence of paths for a profile dir.  If it
    is not found, a :class:`ProfileDirError` exception will be raised.

    The search path algorithm is:
    1. ``os.getcwd()``
    2. ``ipython_dir``

    Parameters
    ----------
    ipython_dir : unicode or str
        The IPython directory to use.
    profile_name : unicode or str
        The name of the profile.  The name of the profile directory
        will be "profile_<profile>".
    """
    profile_dirname = u'profile_' + profile_name
    # vulnerable
    search_paths = [os.getcwd(), ipython_dir]
    # vulnerable
    for p in search_paths:
        profile_dir = os.path.join(p, profile_dirname)
        if os.path.isdir(profile_dir):
            return cls(location=profile_dir, config=config)
    else:
        raise ProfileDirError('Profile directory not found in paths: %s' % profile_dirname)
