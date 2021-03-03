
$(document).ready(function () {
  
  $("#input_nombre").keyup(function () {
    _this = this;
    // Muestra solo los TR, oculta el resto de ellos
    $.each($("#tabla tbody tr"), function () {
      if ($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) // si la fila contiene algun caracter del input
        $(this).hide(); // ocultar
      else 
        $(this).show();  // mostrar
    });
  });                     
});




$('.editarBTN').click(function(e){
    e.preventDefault(); 
    var identificacion = $(this).attr('id');
    abrirModal('/editarEstudiante' , identificacion + "");
});

$('.eliminarBTN').click(function(e){
  e.preventDefault();
  var estudiante = [];
  var identificacion = $('.eliminarBTN').attr('id');
  estudiante.push(identificacion);
  console.log(estudiante);
  
  swal({
    title: "¿Estas seguro de querer eliminar este usuario?",
    text: "Cuidado, Se eliminará el usuario permanentemente",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((confirmar) => {
    if (confirmar) {    // si el director le da a confirmar
      $.ajax({
        method: 'POST',
        url: '/eliminarEstudiante',  // la url a la cual irá la peticion
        data: {
                estudiante: estudiante,   // parametros que se le mandaran a la vista
        },
        success:function(response){
             if(response = "eliminado"){
               swal("¡Fantástico!" , "Se ha eliminado con exito el estudiante" , "success");
               $('.pagina').load('/estudiantes');
             }
        },
        error:function(response){
             swal("Ocurrió un error inesperado :(" , "error");
        }
      });
    } else {    // SI CANCELA EL MODAL 
      swal("¡Puedes seguir revisando, no se realizó ninguna acción!");
    }
  });

});

// Abrir modal creacion
function abrirModal(url , identificacion){
  jQuery.noConflict();         // hace que ignore cuando hay varias instancias de JQuery
  arreglo = {'estudiante' : identificacion}; // guardar la identificacion en un arreglo
//    $('#miModal').modal('show');
//      var url = $(this).data("#formCrearCurso");
    $('#creacion').load(url,arreglo, function(){ // cargar el html en el modal con el parametro
      $(this).modal({
          backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
          keyboard: false     // evita cerrarla con esc.

      })
      $(this).modal('show');  // mostrar el modal
    });

     
   
   //return false;  
}

function cerrarModal() {
  jQuery.noConflict();  
  console.log("antes");
  $('.modal').modal('hide');
  console.log("despues");
  $('.pagina').load('/estudiantes');
  return false;
}
