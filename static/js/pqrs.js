
$(function() {
  var buttonpressed; 
     $('.crear').click(function() {  
           buttonpressed = $(this).attr('name')
          })
          $('#formpqrs').on('submit', function(e) {
              console.log("me envie");
              e.preventDefault();
              var datica = $("#formpqrs :input").serializeArray();
               console.log(datica);
           
               $.ajax({
               type: "POST",
               url: $("#formpqrs").attr("action"),
               data: {
                   csrfmiddlewaretoken:datica[0].value,
                   nombres: datica[1].value,
                   email: datica[2].value,
                   tipoSolicitante: datica[3].value,
                   ciudad: datica[4].value,
                   celular: datica[5].value,
                   tipoSolicitud: datica[6].value,
                   servicioSolicitud: datica[7].value,
                   comentarios: datica[8].value,
               },
               dataType: "html",
               beforeSend: function(response){   
                  console.log("registrando mi pqrs");
              },
              success: function (response) {
                  if(response == "correcto"){
                      swal("Hecho!", "Su solicitud fue registrada con éxito.");
                    }
                  console.log(response);
              },
              error: function (response){
                  console.log(response)
              },
          });
      })
})