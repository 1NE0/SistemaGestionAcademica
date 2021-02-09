
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
  $('#creacion').modal('hide');
  $('#edicion').modal('hide');

  $('.pagina').load('/estudiantes');
  return false;
}
