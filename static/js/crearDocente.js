
/* buscar docente */

$(document).ready(function () {

    $("#input_nombre_docente").on('keyup',function () {
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

/* crud creación */

$(function() {
    var buttonpressed; 
       $('.crear').click(function() {  
             buttonpressed = $(this).attr('name')
            })
            $('#formCrearDocente').on('submit', function(e) {
                console.log("me envie");
                e.preventDefault();
                var datica = $("#formCrearDocente :input").serializeArray();
                 console.log(datica);
             
                 $.ajax({
                 type: "POST",
                 url: $("#formCrearDocente").attr("action"),
                 data: {
                     csrfmiddlewaretoken:datica[0].value,
                     tipoDocumento: datica[1].value,
                     id: datica[2].value,
                     nombres: datica[3].value,
                     apellidos: datica[4].value,
                     edad: datica[5].value,
                     genero: datica[6].value,
                     telefono: datica[7].value,
                     ciudad: datica[8].value,
                     direccion: datica[9].value,
                     correo: datica[10].value,
                     username: datica[11].value,
                     password: datica[12].value
                 },
                 dataType: "html",
                 beforeSend: function(response){   
                    console.log("reealizando crud docente..");
                },
                success: function (response) {
                    if(response == "correcto"){
                        swal("Bien!", "El docente se ha registrado con éxito.", "success");
                        $('.bloque').parents('#contenedor-central').load('/crearDocente');
                      }
                    console.log(response);
                },
                error: function (response){
                    console.log(response)
                },
            });
        })
})


/* Editar y Eliminar docentes */

$('.editarBtn').click(function(e){
  e.preventDefault();

  var identificacion = $(this).attr('id');
  abrirModal('/editarDocente',identificacion + "");
  
});

$('.eliminarBtn').click(function(e){
  e.preventDefault(); 
  var docente = [];
  var identificacion = $('.eliminarBtn').attr('id');

  docente.push(identificacion);
  console.log(docente);

  swal({
    title: "¿Estas seguro de querer eliminar este docente?",
    text: "Cuidado, Se eliminará el docente permanentemente",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((confirmar) => {
    if (confirmar) {    // si el director le da a confirmar
      $.ajax({
        method: 'POST',
        url: '/eliminarDocente',  // la url a la cual irá la peticion
        data: {
                docente: docente,   // parametros que se le mandaran a la vista
        },
        success:function(response){
             if(response = "eliminado"){
               swal("¡Fantástico!" , "Se ha eliminado con exito el docente" , "success");
               $('.bloque').load('/docentes');
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
})

function abrirModal(url,identificacion){

        jQuery.noConflict();
        arreglo = {'docente':identificacion};
        

        $('#creacion').load(url,arreglo,function(){
          $(this).modal({
            backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
            keyboard: false   
          })
          
          $(this).modal('show'); 
          
        });
}

function cerrarModal(){
  jQuery.noConflict(); 
  $('.modal').modal('hide');

  return false;
}



