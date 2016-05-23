$(document).ready(function(){
  $("#form").hide();
  $("#btnLogin").click(function(){
    $("#texts").hide();
    $("#form").show();
  });
  $("#home").click(function(){
    $("#texts").show();
    $("#form").hide();
  });

});