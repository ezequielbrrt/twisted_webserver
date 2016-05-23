$(document).ready(function(){
	$("#centro_registro2").hide();
    $("#boton_agencia").click(function(){
    	$("#centro_registro").hide();
    	$("#centro_registro2").show();	
	});
	$("#boton_usuario").click(function(){
    	$("#centro_registro2").hide();
    	$("#centro_registro").show();	
	});
});

