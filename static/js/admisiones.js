
$('#formsito').on('submit', function(e) {
    e.preventDefault(); // PREVENIR QUE SE RECARGUE LA PAGINA
    var data = $("#form_periodos :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
    console.log(data); // use the console for debugging, F12 in Chrome, not alerts
    
    
    console.log(codigoUsuario);

})

$(".botoncito").click(function(e){
    e.preventDefault();
    codigoUsuario = $(this).siblings('h5').attr('id');
    console.log(codigoUsuario);
    
    $.ajax({
        method: 'POST',
        url: '/aceptarUsuario',
        data: {
                codigoUsuario: codigoUsuario,
                
        },
        success:function(response){
             //this gets called when server returns an OK response
             console.log('it worked!');
             console.log(response);
        },
        error:function(response){
             console.log("it didnt work");
        }
    });
});
