import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class AboutHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('about.html')
class ContactHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('Contact.html')
class DashBoardHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('DashBoard.html')
class HelpHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('help.html')
class MainHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('index.html')
class LoginHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('Login.html')
class RegisterHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('Register.html')
class Register2Handler(tornado.web.RequestHandler):
     def get(self):
          self.render('Register2.html')
class WebpagesHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('Webpages.html')
class WebshowHandler(tornado.web.RequestHandler):
     def get(self):
          self.render('webshow.html')
# Put here yours handlers.



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/',MainHandler),
        (r'/index.html',MainHandler),
        (r'/DashBoard.html',DashBoardHandler),
        (r'/about.html',AboutHandler),
        (r'/Contact.html',ContactHandler),
        (r'/help.html',HelpHandler),
        (r'/Login.html',LoginHandler),
        (r'/Register.html',RegisterHandler),
        (r'/Register2.html',Register2Handler),
        (r'/Webpages.html',WebpagesHandler),
        (r'/webshow.html',WebshowHandler),],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()