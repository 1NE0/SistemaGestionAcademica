$(document).ready(function () {
var botonPresionado;
    $('.registrar').click(function () { 
    botonPresionado = $(this).attr('name')
    
    })
    $('#formCrearCurso').on("submit", function () {
        var data = $("#formCrearCurso :input").serializeArray();
        console.log(data);

        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: {
                csrfmiddlewaretoken: data[0].value,
                cod_curso: data[1].value,
                nom_curso: data[2].value,
                nivel: data[3].value, 
                descripcion: data[4].value,
                cod_Docente: data[5].value,
                grupo: data[6].value, 
                horario_inicial: data[7].value,
                horario_final: data[8].value,
            },
            dataType: "json",
            processData: false, // evita que jQuery intente procesar algo que no puede
            
            beforeSend: function(response){   
                console.log("reealizando...");
            },
            success: function (response) { 
                console.log('cogio el form');
                if(response['Registrado'] == "true"){
                    swal("El curso se ha registrado correctamente", "success");
                }
            },
            error: function (response) {
                console.log(response)
                e.preventDedault(); 
             },
        });
      })
});