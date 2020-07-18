import os.path
from logger import logger
import tornado

import config as cfg


class WebInterface():
    settings = {
        "static_path": os.path.join(CFG.SRC_DIR, "app_dist")
    }

    def __init__(self):
        self.application = tornado.web.Application([
            (r"/", tornado.web.StaticFileHandler, dict(path=self.settings['static_path']))
        ], **self.settings)


        logger.debug("Serving web app at http port 443")