"""
@author: Achyles
"""


from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class MainHandler(RequestHandler):
    def get(self):
        input = self.get_argument('user', 'none')
        self.write('Hello, ' + input)


if __name__ == "__main__":
    handler_mapping = [
                       (r'/', MainHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()