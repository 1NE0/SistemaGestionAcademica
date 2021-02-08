
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

// $(document).ready(function () {
//   $("#botoncito").on("click", function (e) {
//     // cuando se haga click en el boton con ID "botoncito"
//     e.preventDefault(); // no recargue la pagina
//     nombre_input = $("#input_nombre").val(); // obtener el valor que se ingreso en el input con ID "input_nombre"
//     

//     // ignorar
//     return false;
//     console.log("holi");
//   });
// });

$('.editarBTN').click(function(e){
    e.preventDefault();
    var estudianteLista = [];
    var identificacion = $(this).attr('id');
    estudianteLista.push(identificacion);
    $.ajax({
      url: "/editarEstudiante", // a que vista va a pedir los datos
      type: "POST", // con que método se pediran
      data: {
        lista_estudiante : estudianteLista, 
      }, // lo que le asignamos es el nombre que acaba de dar el usuario en el input
      success: function (response) {
        
      },
      error: function (error) {
        console.log(error);
      },
  });
});

// Abrir modal creacion
function abrirModal(url){
  jQuery.noConflict();         // hace que ignore cuando hay varias instancias de JQuery
//    $('#miModal').modal('show');
//      var url = $(this).data("#formCrearCurso");
   $('#creacion').load(url, function(){
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
  return false;
}
