
$(document).ready(function(){

    $('#btn1').on('click', function(c){
        c.preventDefault();
        $("#contenedor-central").load('/cursosDocente');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');

    });

    $('#btn2').on('click', function(asi){
        asi.preventDefault();
        $("#contenedor-central").load('/asignaturasDocente');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn3').on('click', function(actividades){
        actividades.preventDefault();
        $("#contenedor-central").load('/actividadesDocente');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

});