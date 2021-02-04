
$(document).ready(function () {  // cuando el documento esté listo

  GenerarColores();
});

function GenerarColores(){
  $.each($('.programa'),function(i,v){
    var color = '#'+(Math.random()*0xFFFFFF<<0).toString(16);
    $(v).css('background-color',color);
  });
}

function abrirModal(url){
  
  jQuery.noConflict();         // hace que ignore cuando hay varias instancias de JQuery
//    $('#miModal').modal('show');
//      var url = $(this).data("#formCrearCurso");
   $('#creacion').load(url, function(){
       $(this).modal({
           backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
           keyboard: false     // evita cerrarla con esc.
   
       });
       $(this).modal('show');  // mostrar el modal
       console.log("me abri");
   });

   return false;  
}

function cerrarModal() {
  console.log("hola");
  $('#creacion').modal('hide');
  return false;
}