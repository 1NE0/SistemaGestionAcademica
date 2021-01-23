
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

                    // aqui agregar una fila
                    let programas = ["musica","roberto"];
                    console.log(response)
                    agregarFila(response['fecha_inicio'],response['fecha_final']);
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

