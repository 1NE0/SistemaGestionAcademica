


$(document).ready(function(){
    

    $('#formCrear').on("submit", function(e) {
        e.preventDefault();

        var data = $("#formCrear :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
        console.log(data);

        $.ajax({
            url: $("#formCrear").attr("action"),  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
            type: "POST",       // MODO DE ENVIO
            data: {
                csrfmiddlewaretoken: data[0].value,  // QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
                codigo: data[1].value,
                nombre: data[2].value,
                descripcion: data[3].value,
                docente: data[4].value,
            },
            dataType: "html",

            beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                // antes de enviar la peticion
                console.log("reealizando...");

            },
            success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
                    if(response == "ok"){
                    swal("Registrado exitosamente :)", "Se ha registrado correctamente la asignatura", "success");
                    }    
                    
            },
            error: function (response) {
                // si todo sale mal
                console.log(response)
                e.preventDefault();
            },
            });


    });
});




 function abrirModal(url){
    jQuery.noConflict();         // hace que ignore cuando hay varias instancias de JQuery
//    $('#miModal').modal('show');
//      var url = $(this).data("#formCrearCurso");

   $('#creacion').load(url, function(){
       $(this).modal({
           backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
           keyboard: false     // evita cerrarla con esc.
   
       });
       $(this).modal('show');  // mostrar el modal
       console.log("me abri");
   });

   return false;  
}
 
function cerrarModal() {
    jQuery.noConflict(); 
    $('#creacion').modal('hide');
    
    return false;
}





