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
        raise ValueError("MediaFileManager: Missing file %s" % absolute_path)
    except Exception as e:
        LOGGER.error("MediaFileManager: Error getting file %s: %s" % (absolute_path, e))
        raise ValueError("MediaFileManager: Error getting file %s: %s" % (absolute_path, e))
#
    return absolute_path