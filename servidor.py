#! /bin/python
# -*- coding: utf-8 -*-

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import web as index
from twisted.web.resource import Resource
from twisted.web import server, static

import algoritmo.algoritmoG as genetico
import algoritmo.dias as dias




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
        ARREGLO = [0,0,0,0,0,0,0]

        for i in request.args:
            ARREGLO[int(i)] = 1
        genetico.MATERIAS = ARREGLO

        request.write("""
    <!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Schedule</title>

    <!-- Bootstrap Core CSS - Uses Bootswatch Flatly Theme: http://bootswatch.com/flatly/ -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/freelancer.css" rel="stylesheet">
    <link rel="stylesheet" href="css/nifty.min.css"/>


    <!-- Custom Fonts -->
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>
<body id="page-top" class="index">
<!-- Navigation -->

     <div class="container" id="info">

            <div class="row">
                <div class="col-lg-12">
                    <div class="intro-text">
                     <div id="texts">

    """)



        mat = { 1 : "Sistemas Digigales",
        2: "Administración Financiera",
        3: "Compiladores",
        4: "Administracion de servicios en red",
        5: "Análisis de Algorimtos",
        6: "Instrumentación",
        7: "Mat. Avanzadas"

        }

        x = genetico.iniciar()
        print "numero " ,    len(request.args)
        print "x", len(x)
        suma = 0
        for i in x:
            suma += 1
            if suma <=  len(request.args):
                request.write('<h1>%s</h1>'%i)
        #request.write('<h1>%s</h1>'%x[0])
        for i in request.args:
            print i
            if int(i) > 0:
                request.write('<h2>Materia: %s</h2>'% mat[int(i)])
        request.write("""</div> </div>
    <!-- Footer -->
    <footer class="text-center">
        <div class="footer-above">
            <div class="container">
                <div class="row">
                    <div class="footer-col col-md-4">
                        
                    </div>
                    <div class="footer-col col-md-4">
                        <h3>IPN-ESCOM 3CV7</h3>

                    </div>
                </div>
            </div>
        </div>
        <div class="footer-below">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        Copyright &copy;
                    </div>
                </div>
            </div>
        </div>
    </footer>   

                </div>
                 
            </div>
            </div>
        </div>     <script src="js/js.js"></script>
    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src="js/classie.js"></script>
    <script src="js/cbpAnimatedHeader.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="js/jqBootstrapValidation.js"></script>
    <script src="js/contact_me.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="js/freelancer.js"></script>
    <script src="js/login.js"></script>

</body>

</html>""")
        ARREGLO = []
        request.args = []
        request.finish()
        return server.NOT_DONE_YET
        


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