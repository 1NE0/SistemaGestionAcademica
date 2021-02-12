
$(document).ready(function () {  // cuando el documento esté listo

  GenerarColores();
});

function GenerarColores(){  // YA NO SE USA, PUEDE SERVIR PARA OTRA COSA
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





// AQUI ESTA LA LOGICA PARA EL DROG AND DROP


function onDragStart(event) {   // CUANDO SE COMIENZA A ARRASTRAR
  event
    .dataTransfer
    .setData('text/plain', event.target.id);   // AQUI POR LO QUE ENTIENDO SE ROTA EL ID DEL OBJETO DE DONDE SE ARRASTRA

  // cuando se empice a arrastrar el elemento
  // event
  // .currentTarget
  // .style
  // .backgroundColor = 'black';
}

function onDragOver(event) {   // MIENTRAS SE ARRASTRA, PREVENIR QUE SE RECARGUE LA PAGINA
  event.preventDefault();
}

function onDrop(event) {   // CUANDO SE SUELTE
  const id = event // EL OBJETO QUE REALIZA LA OPCION
    .dataTransfer
    .getData('text');   
  
  const draggableElement = document.getElementById(id);  // LO BUSCAMOS EN EL DOCUMENTO
  const dropzone = event.target; // EL TARGET HACE REFERENCIA A DONDE VA A SOLTAR EL ELEMENTO, OSEA EL DROPZONE = PANEL DESTINO
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