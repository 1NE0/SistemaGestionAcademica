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

 

$(document).ready(function(){

  var buttonpressed;
  $('.crear').click(function(){
    buttonpressed = $(this).attr('name')
  })
  $('#form_programas').on('submit',function(e){
      e.preventDefault();
      var data = $("#form_programas :input").serializeArray();
      console.log(data);
      $.ajax({
        url : $(this).attr('action'),
        type: "POST",
        data: { 
          csrfmiddlewaretoken: data[0].value,
          cod_programa: data[1].value,
          nom_programa: data[2].value,
          contenido_Aca: data[3].value,
          duracion: data[4].value,
        },
        dataType: "html",
        beforeSend: function(response){
          console.log("realizando..");
        }, 
        success: function(response){
          if(response == "correcto"){
          swal("Programa creado","Se creó el programa de manera exitosa","success");
          }
          
          console.log(response)

          cerrarModal();


        },
        error: function(response){
          console.log(response)
          e.preventDefault();
        },
      });

  })
});

$('.editar').click(function(e){
  e.preventDefault();
  var codigo = $(this).attr('id');
  modalabrir('/editarPrograma',codigo + "");
});


function modalabrir(url,codigo){
    jQuery.noConflict();

    arreglo = {'programa':codigo};

    $('#creacion').load(url,arreglo,function(){
      $(this).modal({
        backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
        keyboard: false   
      })
      
      $(this).modal('show'); 
      
    });

}

$('.eliminar').click(function(e){
e.preventDefault();
var programa = [];
var codigo = $(this).attr('id');
programa.push(codigo);
console.log(programa);

swal({
  title: "¿Estas seguro de querer eliminar este programa?",
  text: "Cuidado, Se eliminará el programa permanentemente",
  icon: "warning",
  buttons: true,
  dangerMode: true,
})
.then((confirmar) => {
  if (confirmar) {    // si el director le da a confirmar
    $.ajax({
      method: 'POST',
      url: '/eliminarPrograma',  // la url a la cual irá la peticion
      data: {
              programa: programa,   // parametros que se le mandaran a la vista
      },
      success:function(response){
           if(response = "eliminado"){
             swal("¡Fantástico!" , "Se ha eliminado con exito el programa" , "success");
             $('.pagina').load('/programas');
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

function cerrarModal() {
  console.log("hola");
  jQuery.noConflict();
  $('#creacion').modal('hide');
  $('#edicion').modal('hide');
  $('.pagina').load('/programas');
  return false; 
}


