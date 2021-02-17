$(document).ready(function() {
    
    $('#btn1').on('click', function(e) {
        e.preventDefault(); // no recargue la pagina
        $("#contenedor-central").load(''); //cargar la vista "estudiantes" en el div con el id "contenedor" (no olvidarse del numeral adelante)
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
        return false;
        console.log("holi");
    });

    $('#btn2').on('click', function(p){
        p.preventDefault();
        $("#contenedor-central").load('/programasEstudiante');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn3').on('click', function(insc){
        insc.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn4').on('click', function(cursos){
        cursos.preventDefault();
        $("#contenedor-central").load('/cursosEstudiante');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn5').on('click', function(asig){
        asig.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn6').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn7').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

    $('#btn8').on('click', function(prof) {
        prof.preventDefault();
        $("#contenedor-central").load('');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:cyan">Cargando<h1>');
    });

});