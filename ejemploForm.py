
from twisted.web import http
from twisted.web import resource
from twisted.web import server, static


def renderHomePage(request):
	colors = 'red', 'blue', 'green'
	flavors = 'vanilla', 'chocolate', 'strawberry', 'coffee'  
	request.write(""" 
	<html>
		<head>
		<meta charset="utf-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    	<meta name="description" content="">
    	<meta name="Equipo2" content="">
    	<title>Schedule</title>
    	<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

		<!-- jQuery library -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

		<!-- Latest compiled JavaScript -->
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

		<script type="text/javascript" src="js/js.js"></script>

		</head>
		<body> 
  			
			<form action='posthandler' method='post'>  Your name:  <p>  
			<input type='text' name='name'>  
			</p>  What's your favorite color?  <p>   
		""")
	request.write("console.log('hola mundo');") 
	for color in colors:  
		request.write(  "<input type='radio' name='color' value='%s'>%s<br />" % (  color, color.capitalize( )))  
	request.write("""  </p>  What kinds of ice cream do you like?  <p>  """)  
	for flavor in flavors:  
		request.write(  "<input type='checkbox' name='flavor' value='%s'>%s<br />" % (  flavor, flavor.capitalize( )))  
	request.write("""  </p>  <input type='submit' />  </form>  </body>  </html>  """)  
	request.finish( )    

def handlePost(request):  
	request.write("""<html>
		<head>
		<meta charset="utf-8">
    	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    	<meta name="description" content="">
    	<meta name="Equipo2" cPAGEontent="">
    	<title>Schedule</title>
    	<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

		<!-- jQuery library -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

		<!-- Latest compiled JavaScript -->
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

		</head>
		<body>   """)
	values = []    
	for key, values2 in request.args.items( ):
		print "primer for"
		values.append(values2)
	 	request.write('<h2>%s</h2>' % key)  
	 	request.write('<ul>')
	print "request",request.args.items( )
	print values  
	for value in values:
		request.write('<li>%s</li>' % value)  
		request.write('</ul>')    
	request.write('</body>  </html>')  
	request.finish()    

class FunctionHandledRequest(http.Request):  
	pageHandlers = {  '/': renderHomePage,  '/posthandler': handlePost,  }    
	def process(self):
		self.setHeader('Content-Type', 'text/html')
		if self.pageHandlers.has_key(self.path):  
			handler = self.pageHandlers[self.path]  
			handler(self)  
		else:  
			self.setResponseCode(http.NOT_FOUND) 
			self.write("<h1>Not Found</h1>Sorry, no such page.")  
		self.finish()

class MyHttp(http.HTTPChannel):
	requestFactory = FunctionHandledRequest 

class MyHttpFactory(http.HTTPFactory):
	def getChild(self, name, request):
		if name == '':
			return self
		return resource.Resource.geChild(self, name, request)
	protocol = MyHttp



from twisted.internet import reactor
root = MyHttpFactory()
root.putChild('js', static.File("./js"))
site = server.Site(root)
reactor.listenTCP(8000, site)
reactor.run( )