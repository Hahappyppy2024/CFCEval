import tornado.web
from streamlit.logger import get_logger
from streamlit.media_file_manager import media_file_manager


LOGGER = get_logger(__name__)
def validate_absolute_path(self, root, absolute_path):
    try:
        media_file_manager.get(absolute_path)
    except KeyError:
        error_message = f"MediaFileManager: Missing file {absolute_path}"
        LOGGER.error(error_message)
        #
        raise ValueError(error_message)
    except Exception as e:
        error_message = f"MediaFileManager: Error getting file {absolute_path}: {e}"
        LOGGER.error(error_message)
        raise ValueError(error_message)
#
    return absolute_path