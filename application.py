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

    def write_error(self, status_code, **kwargs):
        self.write("'MainHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class AboutHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('about.html')

    def write_error(self, status_code, **kwargs):
        self.write("'AboutHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class ContactHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Contact.html')

    def write_error(self, status_code, **kwargs):
        self.write("'ContactHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class DashBoardHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('DashBoard.html')

    def write_error(self, status_code, **kwargs):
        self.write("'DashBoardHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class HelpHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('help.html')

    def write_error(self, status_code, **kwargs):
        self.write("'HelpHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class LoginHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Login.html')

    def write_error(self, status_code, **kwargs):
        self.write("'LoginHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class RegisterHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Register.html')

    def write_error(self, status_code, **kwargs):
        self.write("'RegisterHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class Register2Handler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Register2.html')

    def write_error(self, status_code, **kwargs):
        self.write("'Register2Handler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class WebpagesHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('Webpages.html')

    def write_error(self, status_code, **kwargs):
        self.write("'WebpagesHandler' caused a %d error." % status_code)


# noinspection PyMissingOrEmptyDocstring
class WebshowHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('webshow.html')

    def write_error(self, status_code, **kwargs):
        self.write("'WebshowHandler'You caused a %d error." % status_code)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler),
                  (r'/index.html', MainHandler),
                  (r'/DashBoard.html', DashBoardHandler),
                  (r'/about.html', AboutHandler),
                  (r'/Contact.html', ContactHandler),
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
