import os
from io import StringIO, BytesIO

import tornado.web
import tornado.ioloop
import asyncio

import uvloop as uvloop
from PIL import Image
from tornado.escape import json_decode


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def rgb_color(file):
    im = Image.open(BytesIO(file))

    pix = im.convert('RGB').getdata()
    size = im.size
    colors = {}
    for i in range(len(pix)):
        if colors.get(pix[i]):
            colors[pix[i]]['count'] += 1
        else:
            colors[pix[i]] = {
                'count': 1,
                'hexadecimal': rgb2hex(r=pix[i][0], g=pix[i][1], b=pix[i][2]),
                'RGB': f"{pix[i][0]} {pix[i][1]} {pix[i][2]}"
            }
    pass
    count_validos = 0
    colors_result = {}
    for color in colors:
        c = colors[color]
        # irá contabilizar

        porcetagem = round(c['count'] / len(pix) * 100, 3)
        # irá pegar as cores que represente pelomenos 0.1 da imagem
        if porcetagem > 0.099:
            count_validos += c['count']
            colors_result[color] = c
    result = []
    for color in colors_result:
        c = colors_result[color]
        c['porcentagem'] = round(c['count'] / count_validos * 100, 3)
        result.append(c)
    return result


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        #Se usar formulario html
        # file = ["fileImage"][0]['body']
        #POST REQUISICAO HTTP
        file = self.request.body
        r = rgb_color(file)
        self.write({'result':r})

    def get(self):
        # self.write({1: 'alex'})
        self.render("index.html")


app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/upload/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])
if (__name__ == "__main__"):
    # def run():
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    print("Listening on port 8000")
    tornado.ioloop.IOLoop.instance().start()
