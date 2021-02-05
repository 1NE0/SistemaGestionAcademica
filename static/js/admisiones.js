
$('#formsito').on('submit', function(e) {
    e.preventDefault(); // PREVENIR QUE SE RECARGUE LA PAGINA
    var data = $("#form_periodos :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
    console.log(data); // use the console for debugging, F12 in Chrome, not alerts
    
    
    console.log(codigoUsuario);

})

$(".botoncito").click(function(e){
    e.preventDefault();
    codigoUsuario = $(this).siblings('h5').attr('id');  // obtener el hermano de este objeto
    console.log(codigoUsuario);
    swal({
        title: "¿Estas seguro de aceptar el pago de este usuario?",
        text: "transformarás este usuario en un estudiante de la academia",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((confirmar) => {
        if (confirmar) {    // si el director le da a confirmar
            $.ajax({
                method: 'POST',
                url: '/aceptarUsuario',  // la url a la cual irá la peticion
                data: {
                        codigoUsuario: codigoUsuario,   // parametros que se le mandaran a la vista
                },
                success:function(response){
                     //     SINO SALE NINGUN ERROR
                     swal("¡se realizó con exito la acción!", {
                        icon: "success",
                      });
                      $('#' + codigoUsuario).remove();  // remover el div que tiene la informacion del usuario a inscribirse 
                },
                error:function(response){
                     swal("Ocurrió un error inesperado :(" , "error");
                }
            });
          
        } else {    // SI CANCELA EL MODAL 
          swal("¡Puedes seguir revisando, no se realizó ninguna acción!");
        }
      });


    
});
