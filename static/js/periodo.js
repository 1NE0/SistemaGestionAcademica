
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

  // actualizar informacion
  $('.paginita').load('/periodos');
  return false;
}


function onDragStart(event) {
  event
    .dataTransfer
    .setData('text/plain', event.target.id);

  // cuando se empice a arrastrar el elemento
  // event
  // .currentTarget
  // .style
  // .backgroundColor = 'black';
}

function onDragOver(event) {
  event.preventDefault();
}

function onDrop(event) {
  const id = event
    .dataTransfer
    .getData('text');
  
  const draggableElement = document.getElementById(id);
  const dropzone = event.target; // el evento se genera en el dropzone
  dropzone.appendChild(draggableElement); // agregarle el elemento que estamos arrastrando

  event  // borrar la transferencia
  .dataTransfer
  .clearData();
}



$(".botoncito").click(function(e){
  e.preventDefault();
  var listaProgramas = [];
  $('.example-dropzone').children('div').each(function(obj){
      listaProgramas.push($(this).attr('id'));
  });
  console.log(listaProgramas);
   $.ajax({
      method: 'POST',
      url: '/asignarProgramas',
      data: {
              listaProgramas: listaProgramas,
      },
      success:function(response){
           //this gets called when server returns an OK response
           if(response == "actualizado"){
            swal("¡" + response + " con éxito!", "Se ha actualizado correctamente el periodo :)", "success");
           }
      },
      error:function(response){
           swal("Ocurrió un error inesperado :(" , "Error");
      }
  });
});