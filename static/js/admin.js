


$(document).ready(function() {
    

    $('li a').click(function(){
        console.log("me dieron click");
        $('.darkerlishadow').removeClass('darkerlishadow');
        $(this).parents('li').addClass('darkerlishadow');
    });



    $('#btn1').on('click', function(e) {
        e.preventDefault(); // no recargue la pagina
        $("#contenedor-central").load('/estudiantes'); //cargar la vista "estudiantes" en el div con el id "contenedor" (no olvidarse del numeral adelante)
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
        // lo de arriba es el "cargando", mientras que se carga, poner el html que está entre las comillas



        // $.ajax({
        //     url: "/estudiantes",
        //     type:"get",
        //     dataType: "json",
        //     success: function(response){
        //         console.log(response);
        //     },
        //     error: function(error){
        //         console.log(error);
        //     }
        // });

        // ignorar
        return false;
        console.log("holi");
    });

    $('#btn2').on('click', function(p){
        p.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/programas');
    });

    $('#btn3').on('click', function(insc){
        insc.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/admisiones');
    });

    $('#btn4').on('click', function(cursos){
        cursos.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/cursos');
    });

    $('#btn5').on('click', function(asig){
        asig.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/asignaturas');
    });

    $('#btn6').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/crearDocente');
    });

    $('#btn7').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/periodos');
        
    });

    $('#btn8').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/pagos');
    });

    $('#btn9').on('click', function(est) {
        est.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/estadisticas');
    });

});


/*$(document).ready(function() {
    serializar();

});*/

