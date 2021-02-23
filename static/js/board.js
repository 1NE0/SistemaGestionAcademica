
$(document).ready(function() {
    
    $('#btn1').on('click', function(p){
        p.preventDefault(); // no recargue la pagina
        $("#contenedor-central").load('/programasEstudiante'); //cargar la vista "estudiantes" en el div con el id "contenedor" (no olvidarse del numeral adelante)
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
        return false;
        console.log("holi");
    });

    $('#btn2').on('click', function(cursitos){
        cursitos.preventDefault();
        $("#contenedor-central").load('/cursosEstudiante');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
        return false;
    });

    $('#btn3').on('click', function(asignaturas){
        asignaturas.preventDefault();
        $("#contenedor-central").load('/asignaturasEstudiante');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn4').on('click', function(pagos){
        pagos.preventDefault();
        $("#contenedor-central").load('/pagosEstudiante');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn5').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

});