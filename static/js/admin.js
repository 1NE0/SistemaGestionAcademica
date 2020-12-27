
function serializar(){
    
 }

$(document).ready(function() {
    $('#btn1').on('click', function(e) {
        e.preventDefault(); // no recargue la pagina
        $("#contenedor-central").load('/estudiantes');
        $("#contenedor-central").html('<h1 style="text-align:center;padding-top:300px;color:white">Cargando<h1>');
        
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

        
        return false;
        console.log("holi");
    });

    

    

    
});

// $(document).ready(function(){
//     serializar();
// });