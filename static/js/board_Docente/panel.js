
$(document).ready(function(){

    $('li a').click(function(){
        console.log("me dieron click");
        $('.darkerlishadow').removeClass('darkerlishadow');
        $(this).parents('li').addClass('darkerlishadow');
    });

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