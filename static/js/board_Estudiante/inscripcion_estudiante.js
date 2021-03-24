


$(document).ready(function(){
    $('.boton').click(function(){
        
        $('.check').each(function(){
            
            if($(this).prop('checked') == true){
                console.log("estoy activo");
            }else{
                console.log("no estoy activo");
            }
        });
    });
    
});