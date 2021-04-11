var ctx = document.getElementById('myChartcito').getContext('2d');
/* var ctx2 = document.getElementById('myChart2').getContext('2d'); */
console.log("hola");

 
$(document).ready(function (){
    $.ajax({
        url: '/obtenerEstadisticas',  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
        type: "POST",       // MODO DE ENVIO
        dataType: "json",
        beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
            // antes de enviar la peticion
            console.log("reealizando...");

        },
        success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
            
            var jsonRecibido = jQuery.parseJSON(response);
            var cantidadEstudiantes = jsonRecibido['estudiantesCantidad'];
            var cantidadUsuarios = jsonRecibido['usuariosTotales'];
            var cantidadProgramas = jsonRecibido['programasTotales'];
            var cantidadCursos = jsonRecibido['cursosTotales'];
            var cantidadAsignaturas = jsonRecibido['asignaturasTotales'];
            var cantidadDocentes = jsonRecibido['docentesTotales'];
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Estudiantes', 'Usuarios', 'Programas', 'Cursos', 'Asignaturas', 'Docentes'],
                    datasets: [{
                        label: 'cantidad',
                        data: [cantidadEstudiantes, cantidadUsuarios, cantidadProgramas, cantidadCursos, cantidadAsignaturas, cantidadDocentes],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
            
            
            
            
        },
        error: function (response) {
            // si todo sale mal
            console.log(response)
            e.preventDefault();
        },
        });
});


