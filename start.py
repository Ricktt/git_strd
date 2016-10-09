#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("s1.html")
    def post(self):
        us = self.get_argument("user",None)
        pw = self.get_argument("pwd",None)
        if us == "dyq" and pw == "123":
            self.redirect("http://www.baidu.com")   #redirect  返回指定的URL
            # self.render("s2.html")    # render 返回指定的html文件
        else:
            self.alert("登录失败")

class index(tornado.web.RequestHandler):
    def post(self):
        self.render("ind.html")


settings = {
    'static_path':"statics",
    'template_path':'views'
}

application = tornado.web.Application([
    (r"/login", MainHandler),
    (r"/index", index)
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()