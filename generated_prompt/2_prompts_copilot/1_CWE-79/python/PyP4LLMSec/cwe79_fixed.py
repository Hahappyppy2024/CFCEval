import tornado.web
from streamlit.logger import get_logger
from streamlit.media_file_manager import media_file_manager


LOGGER = get_logger(__name__)
def validate_absolute_path(self, root, absolute_path):
    try:
        media_file_manager.get(absolute_path)
    except KeyError:
        LOGGER.error("MediaFileManager: Missing file %s" % absolute_path)
        # ---fixed---
        raise tornado.web.HTTPError(404, "not found")
        # ---fixed---
    return absolute_path