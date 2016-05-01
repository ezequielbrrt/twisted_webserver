from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import web as index

import cgi

class FormPage(Resource):
    def render_GET(self, request):
        return index.index()

    def render_POST(self, request):
    	#met.proceso()
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)
        #return '<html><body>You submitted: %s</body></html>' % (cgi.escape(str(met.proceso())),)

root = Resource()
root.putChild("index", FormPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
