import tornado.web
from streamlit.logger import get_logger
from streamlit.media_file_manager import media_file_manager


LOGGER = get_logger(__name__)
def validate_absolute_path(self, root, absolute_path):
    try:
        media_file_manager.get(absolute_path)
    except KeyError:
        LOGGER.error("MediaFileManager: Missing file %s" % absolute_path)
        #
       if not os.path.abspath(
           absolute_path).startswith(os.path.
                                     abspath(root)):
            LOGGER.error("MediaFileManager: Invalid
                         absolute path %s" % absolute_path)
                         return False
                         return True
        #
    return absolute_path