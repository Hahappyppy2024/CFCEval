import tornado.web
from streamlit.logger import get_logger
from streamlit.media_file_manager import media_file_manager

log = get_logger(__name__)

def validate_media_file_path(self, media_root_dir, media_abs_path):
    try:
        media_file_manager.get(media_abs_path)
    except KeyError:
        log.error("MediaFileManager: Missing file %s" % media_abs_path)

    return media_abs_path
