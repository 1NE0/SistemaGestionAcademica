


$(document).ready(function(){

    $('.mensaje').hide();
    $('#cargando').hide();

    $('#form').submit(function(e){
        e.preventDefault();

        var datica = $("#form :input").serializeArray();
        console.log(datica);

        $.ajax({
            type: "POST",
            url: $("#form").attr("action"),
            data: {
                csrfmiddlewaretoken:datica[0].value,
                username: datica[1].value,
                password: datica[2].value
            },
            dataType: "html",
            beforeSend: function(response){   
                $('#cargando').show();
           },
           success: function (response) {
               
                if(response == "usuarioNoExiste"){
                    $('.mensaje').children('p').text('NO SE ENCUENTRA UN USUARIO CON ESTE USERNAME');
                    $('.mensaje').show();
                    $('#cargando').hide();
                }else if (response == "contraseñaIncorrecta"){
                    $('.mensaje').children('p').text('EL USERNAME Y LA CONTRASEÑA NO COINCIDEN');
                    $('.mensaje').show();
                    $('#cargando').hide();
                }else{
                    window.location.replace("/home");
                }
               console.log(response);
           },
           error: function (response){
               console.log(response)
           },
       });
    });

});