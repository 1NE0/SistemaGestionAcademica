
$(document).ready(function () {  // cuando el documento esté listo
      var buttonpressed;  // crear esta variable para guardar el nombre del boton que se presionó
       $('.registrar').click(function() {  // 
             buttonpressed = $(this).attr('name')
       })
       $('#form_periodos').on('submit', function(e) {
                e.preventDefault(); // PREVENIR QUE SE RECARGUE LA PAGINA
                var data = $("#form_periodos :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
                console.log(data); // use the console for debugging, F12 in Chrome, not alerts
                
                $.ajax({
                url: $(this).attr("action"),  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
                type: "POST",       // MODO DE ENVIO
                data: {
                    csrfmiddlewaretoken: data[0].value,  // QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
                    Fecha_inicio: data[1].value,
                    Fecha_final: data[2].value,
                },
                dataType: "json",
                beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                    // antes de enviar la peticion
                    console.log("reealizando...");
                },
                success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
                    
                    // si todo sale bien
                    if(response['error_boludo'] == "error"){  // DESDE LA VISTA, YO MADE UN JSON, QUE DECIA "ERROR", SI YA SE ENCONTRABA UN PERIDOO REGISTRADO
                        console.log("CAPTURE EL JSON")
                        swal("Ocurrió un error :(", "Ya hay un periodo con esta fecha.", "error");
                    }else if(response['registrado'] == "true"){    // SI EL JSON, NO ES UN ERROR, ENTONCES ES QUE NO ESTA REGISTRADO EL PERIODO
                        swal("¡Bien hecho!", "Se registro correctamente el periodo", "success");
    
                        // actualizar pagina
                        
                    }
                    
                    
                },
                error: function (response) {
                    // si todo sale mal
                    console.log(response)
                    e.preventDefault();
                },
                });
       })
    
    function agregarFila(fecha_inicio,fecha_final){
        var htmlTags = '<tr style="color:white;font-weight:bold;background-color:#092638;">'+
                            '<td>' + fecha_inicio + '</td>'+
                            '<td>' + fecha_final + '</td>'
                        '</tr>';
        $('#tablita tbody').append(htmlTags);
        console.log("actualizando tabla")
    }
    
    function prueba(){
        console.log("me ejecute");
    }
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
      url: '/asignarProgramas', // holi
      data: {
              listaProgramas: listaProgramas,
      },
      success:function(response){
           //this gets called when server returns an OK response
           if(response == "actualizado"){
            swal("¡" + response + " con éxito!", "Se ha actualizado correctamente el periodo :)", "success");
           }else if(response == "guardado"){
            swal("¡" + response + " con éxito!", "Se ha guardado correctamente el periodo :)", "success");
           }
      },
      error:function(response){
           swal("Ocurrió un error inesperado :(" , "Error");
      }
  });
});



/* LOGICA DE CRUD  */



  