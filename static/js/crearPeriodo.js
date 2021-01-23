
$(function() {
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
            beforeSend: function(response){
                // antes de enviar la peticion
                console.log("reealizando...");
            },
            success: function(response){
                // si todo sale bien
                if(response['error_boludo'] == "error"){
                    console.log("CAPTURE EL JSON")
                    swal("Ocurrió un error :(", "Ya hay un periodo con esta fecha.", "error");
                }else{
                    swal("¡Bien hecho!", "Se registro correctamente el periodo", "success");
                }
                
                
            },
            error: function (response) {
                // si todo sale mal
                console.log(response)
                e.preventDefault();
            },
            });
   })
})
