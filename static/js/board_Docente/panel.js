
$(document).ready(function(){

    $('#btn1').on('click', function(c){
        c.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/cursosDocente');

    });

    $('#btn2').on('click', function(asi){
        asi.preventDefault();
        //$("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/asignaturasDocente');
    });

    $('#btn3').on('click', function(actividades){
        actividades.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/actividadesDocente');
    });

});