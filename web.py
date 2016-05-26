# -*- coding: utf-8 -*-

from twisted.web import http
from twisted.web import resource
from twisted.web import server, static
#import variables as var


def index(request):
  """f = open("materias.txt", "r")
  materias = f.read()
  f.close()
  materias = materias.split("\n")
  materias = filter(None, materias) # fastest
  """
   #header
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
    """)

  request.write(
  """

<body id="page-top" class="index">

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">

                <a class="navbar-brand" href="#page-top" id="home">Schedule</a>
            </div>


            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

  """)
  request.write("""

  <div class="table-responsive" >
    <table class="table table-hover" id="tabla">
    <form method="post">
      <thead>
        <tr>
          <th>#</th>
          <th>Materia</th>
          <th>Tiempo</th>
          <th>Frecuencia</th>
          <th>Créditos</th>
          <th></th>
          <th>Seleccionado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>D. Sistemas Digitales</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.50</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="option1" name="1">Seleccionar
                </label>
              </div>
          </td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Admin. Financiera</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.36</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="option1" name="2">Seleccionar
                </label>
              </div>
          </td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Compiladores</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.39</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="option1" name="3">Seleccionar
                </label>
              </div>
          </td>
        </tr>
        <tr>
          <th scope="row">4</th>
            <td>Redes 2</td>
          <td>90 minutos</td>
          <td>3</td>
            <td>4.39</td>
            <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="option1" name="4">Seleccionar
                </label>
              </div>
          </td>
  
        </tr>
        <tr>
          <th scope="row">5</th>
          <td>Algoritmos</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.39</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="option1" name="5">Seleccionar
                </label>
              </div>
          </td>
        </tr>
        <tr>
          <th scope="row">6</th>
          <td>Instrumentación</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.39</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="instru" name="6">Seleccionar
                </label>
              </div>
          </td>
        </tr>
         <tr>
          <th scope="row">7</th>
          <td>Mat. Avanzadas</td>
          <td>90 minutos</td>
          <td>3</td>
          <td>4.46</td>
          <td></td>
          <td><div class="checkbox">
                <label>
                  <input type="checkbox" id="blankCheckbox" value="avanzadas" name="7">Seleccionar
                </label>
              </div>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="row">
      <div class="col-md-8">
      </div>
      <div class="col-md-offset-2 col-md-2">
          <input type="submit">
    </form>
      </div>
    </div>
  </div>

      """)
  request.write("""
        <!-- Footer -->
    <footer class="text-center">
        <div class="footer-above">
            <div class="container">
                <div class="row">
                    <div class="footer-col col-md-4">
                        
                    </div>
                    <div class="footer-col col-md-4">
                        <h3>IPN-ESCOM 3CV7</h3>
                        <p>Barreto Aviles Ezequiel Adrian</p>
                        <p>Morales Baez Alan</p>
                        <p>Venegas Melendez Marcos</p>
                        <p>Salgado Flores Mauricio</p>
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



    
    <script src="js/js.js"></script>
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

</html>
    """)
  request.finish( ) 