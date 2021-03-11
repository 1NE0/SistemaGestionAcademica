


$(document).ready(function(){
    $('#formCrear').on('submit', function(e) {
        e.preventDefault();
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





