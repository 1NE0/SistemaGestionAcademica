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
    
});*/

function registrar(){
    $.ajax({
        type: "POST",
        url: $("#formCrearCurso").attr('action'),
        data: $("#formCrearCurso").serialize(),
        dataType: "string",
        success: function (response) {
            alert('.....');
        }
    });
}

$(function() {

    var inputs = $("#formCrearCurso :input").val().serialize();
    console.log(inputs);
    
    $.ajax({
        type: "POST",
        url: $("#formCrearCurso").attr('action'),
        data: {
            csrfmiddlewaretoken: data[0].value,
            nivel : inputs[1].value,
            descripcion : inputs[2].value 
        },
        dataType: "json",
        success: function (response) {
            
        }
    });



})

