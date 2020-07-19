import os.path
from logger import logger
import tornado.ioloops
import tornado.web
import tornado.websocket
import tornado.escape

import config as cfg

class Application(tornado.web.Application):
    def __init__(self, car):
        settings = dict(
            static_path = os.path.join(cfg.SRC_DIR, "app_dist"),
            template_path = os.path.join(cfg.SRC_DIR, "app_dist"),
            default_handler_class = MainHandler
        )

        handlers = [
            (r"/", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
            (r"/carsocket", CarSocketHandler)
        ]

        self.car = car

        super(Application, self).__init__(handlers, **settings)

    def update_clients(self, data):
        CarSocketHandler.update_clients(data)

    
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class CarSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        logger.debug("Websocket connection opened")
        CarSocketHandler.clients.add(self)

    def on_close(self):
        logger.debug("Websocket connection closed")
        CarSocketHandler.clients.remove(self)

    def on_message(self, msg):
        data = tornado.escape.json_decode(msg)

        self.application.car.updateControls(data)

    @classmethod
    def update_clients(cls, data):
        for client in CarSocketHandler.clients:
            try:
                client.write_message(data)
            except:
                logger.warning("Error updating websocket client", exc_info=True)

def startWebInterface(car):
    app = Application(car)
    app.listen(cfg.APP_PORT)
    tornado.ioloop.IOLoop.current().start()

    logger.debug(f"Web app listening on port {cfg.APP_PORT}")

    return app