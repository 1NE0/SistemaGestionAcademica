
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
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/cursosEstudiante');
        return false;
    });

    $('#btn3').on('click', function(asignaturas){
        asignaturas.preventDefault();
        //$("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/asignaturasEstudiante');
    });

    $('#btn4').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('');
    });

    $('#btn5').on('click', function(pagos){
        pagos.preventDefault();
        $("#contenedor-central").load('/cargando');
        $("#contenedor-central").load('/inscripcionManual');
    });

});