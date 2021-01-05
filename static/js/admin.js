
function serializar(){
    
}



$(document).ready(function() {

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
        $("#contenedor-central").load('/programas');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
    });

    $('#btn3').on('click', function(insc){
        insc.preventDefault();
        $("#contenedor-central").load('/admisiones');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
    });

    $('#btn4').on('click', function(cursos){
        cursos.preventDefault();
        $("#contenedor-central").load('/cursos');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
    });

    $('#btn5').on('click', function(asig){
        asig.preventDefault();
        $("#contenedor-central").load('/asignaturas');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
    });

    $('#btn6').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('/docentes');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
    });

});


/*$(document).ready(function() {
    serializar();

});*/

