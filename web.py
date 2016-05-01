

def index():
	html = """
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

		</head>
		<body>	
			
			<form method="POST">
  				<input name="the-field2" type="text" />
  				<input name="the-field" type="text" />
  				
			</form>
		</body>
		</html>"""
	html2 = '<html><body><form method="POST"><input name="the-field" type="text" /></form></body></html>'
	return html