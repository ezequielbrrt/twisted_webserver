#! /bin/python
# -*- coding: utf-8 -*-

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import web as index
from twisted.web.resource import Resource
from twisted.web import server, static


import cgi
class Home(Resource):
    isLeaf = False

    def getChild(self, name, request):
        if name == '':
            return self
        return resource.Resource.geChild(self, name, request)

    def render_GET(self, request):
        index.index(request)
        return server.NOT_DONE_YET

    def render_POST(self,request):
    	print request.args

root = Resource()
root.putChild("schedule", Home())

# Agregando directorios al servidor
root.putChild('css', static.File("./css"))
root.putChild('img', static.File("./img"))
root.putChild('js', static.File("./js"))
root.putChild('fonts', static.File("./fonts"))
root.putChild('font-awesome', static.File("./font-awesome"))
root.putChild('inicio', static.File("./inicio/inicio.html"))
site = server.Site(root)
reactor.listenTCP(8000, site)
reactor.run()