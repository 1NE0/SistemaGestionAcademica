

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
                    }
                    console.log(response);
                },
                error: function (response){
                    console.log(response)
                },
            });
        })
})