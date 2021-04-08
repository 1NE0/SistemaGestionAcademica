


$(function() {
  var buttonpressed; 
     $('.crear').click(function() {  
           buttonpressed = $(this).attr('name')
          })
          $('#formContacto').on('submit', function(e) {
              console.log("me envie");
              e.preventDefault();
              var datica = $("#formContacto :input").serializeArray();
               console.log(datica);
           
               $.ajax({
               type: "POST",
               url: $("#formContacto").attr("action"),
               data: {
                   csrfmiddlewaretoken:datica[0].value,
                   nombres: datica[1].value,
                   email: datica[2].value,
                   mensaje: datica[3].value
               },
               dataType: "html",
               beforeSend: function(response){   
                  console.log("mandando mi inquietud...");
              },
              success: function (response) {
                  if(response == "correcto"){
                      swal("Hecho!", "Tu inquietud fue mandada.", "success");
                    }
                  console.log(response);
              },
              error: function (response){
                  console.log(response)
              },
          });
      })
})
