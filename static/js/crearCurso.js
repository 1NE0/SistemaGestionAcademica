/*$(function() {

    $('#formCrearCurso').submit(function (e) { 
        e.preventDefault();
        var data = $("#formCrearCurso :input").serializeArray();
        console.log(data);

        $.ajax({
            type: "POST",
            url: '/crearcurso', 
            data: {
                csrfmiddlewaretoken: data[0].value,
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
})


$('.enviar').on('submit', function () {
    alert('me abrooooo todo');

});

$(document).on('submit', '#formCrearCurso', function (e) {
    e.preventDefault();
        var datitca = $("#formCrearCurso :input").serializeArray();
    $.ajax({
        type: "POST",
        url: "{% url 'crearcurso' %}",
        data: 
            { csrfmiddlewaretoken: data[0].value },
            
        dataType: "dataType",
        success: function (response) {
            console.log('cogio el form');
            
        },
        error: function (response) {
            console.log(response)
        },
    });
    
});

function registrar(){

    $.ajax({
        type: "POST",
        url: $("#formCrearCurso").attr('action'),
        data: $("#formCrearCurso").serialize(),
        dataType: "json",
        success: function (response) {
            swal("Registrado");
        }
    });
}*/

$(function() {
var buttonpressed; 
   $('.enviar').click(function() {  
         buttonpressed = $(this).attr('name')
   })
   $('#formCrearCurso').on('submit', function(e) {
       console.log("me envie");
       e.preventDefault();
       var inputs = $("#formCrearCurso :input").serializeArray();
        console.log(inputs);
    
        $.ajax({
        type: "POST",
        url: $("#formCrearCurso").attr("action"),
        data: {
            csrfmiddlewaretoken:inputs[0].value,
            cod_curso: inputs[1].value,
            nom_curso: inputs[2].value
        },
        dataType: "html",
        beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
            // antes de enviar la peticion
            console.log("reealizando...");
        },
        success: function (response) {
            if(response == "correcto"){
                swal("Correcto!", "El curso se ha registrado con éxito.", "success");
            }
            console.log(response);
        },
        error: function (response) {
            console.log(response)
        }
    });

   })
})


