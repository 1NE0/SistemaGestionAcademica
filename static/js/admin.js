
function serializar(){
    
 }

$(document).ready(function() {
    $('#btn1').on('click', function(e) {
        e.preventDefault(); // no recargue la pagina
        $("#contenedor-central").load('/estudiantes'); //cargar la vista "estudiantes" en el div con el id "contenedor" (no olvidarse del numeral adelante)
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
        // lo de arriba es el "cargando", mientras que se carga, poner el html que está entre las comillas



        // $.ajax({
        //     url: "/estudiantes",
        //     type:"get",
        //     dataType: "json",
        //     success: function(response){
        //         console.log(response);
        //     },
        //     error: function(error){
        //         console.log(error);
        //     }
        // });

        // ignorar
        return false;
        console.log("holi");
    });

    

    

    
});

// $(document).ready(function(){
//     serializar();
// });