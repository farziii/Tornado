# coding=utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


# noinspection PyMissingOrEmptyDocstring
class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('index.html')


# noinspection PyMissingOrEmptyDocstring
class AboutHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('about.html')


# noinspection PyMissingOrEmptyDocstring
class ContactHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Contact.html')


# noinspection PyMissingOrEmptyDocstring
class ContactResultHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('ContactResult.html')


# noinspection PyMissingOrEmptyDocstring
class DashBoardHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('DashBoard.html')


# noinspection PyMissingOrEmptyDocstring
class HelpHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('help.html')


# noinspection PyMissingOrEmptyDocstring
class LoginHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Login.html')


# noinspection PyMissingOrEmptyDocstring
class RegisterHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Register.html')


# noinspection PyMissingOrEmptyDocstring
class Register2Handler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Register2.html')


# noinspection PyMissingOrEmptyDocstring
class WebpagesHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Webpages.html')


# noinspection PyMissingOrEmptyDocstring
class WebshowHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('webshow.html')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler),
                  (r'/index.html', MainHandler),
                  (r'/DashBoard.html', DashBoardHandler),
                  (r'/about.html', AboutHandler),
                  (r'/Contact.html', ContactHandler),
                  (r'/ContactResult.html', ContactResultHandler),
                  (r'/help.html', HelpHandler),
                  (r'/Login.html', LoginHandler),
                  (r'/Register.html', RegisterHandler),
                  (r'/Register2.html', Register2Handler),
                  (r'/Webpages.html', WebpagesHandler),
                  (r'/webshow.html', WebshowHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
