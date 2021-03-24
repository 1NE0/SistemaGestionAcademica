


$(document).ready(function(){
    $('.matricular').click(function(e){
        e.preventDefault();
        swal({
            title: "Are you sure?",
            text: "Once deleted, you will not be able to recover this imaginary file!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          })
          .then((willDelete) => {
            if (willDelete) {
                var listaCursos = [];
                var listaAsignaturas = [];
                $('.cursos-disponibles .check').each(function(){
                    
                    if($(this).prop('checked') == true){
                        listaCursos.push($(this).attr('id'));
                    }else{
                        console.log("no estoy activo");
                    }
        
                });
                $('.asignaturas-disponibles .check').each(function(){
                    
                    if($(this).prop('checked') == true){
                        listaAsignaturas.push($(this).attr('id'));
                    }else{
                        console.log("no estoy activo");
                    }
        
                });
                $.ajax({
                    method: 'POST',
                    url: '/guardarInscripcionCurso/', // holi
                    data: {
                            listaCursos: listaCursos,
                    },
                    success:function(response){
                         //this gets called when server returns an OK response
                         if(response == "correcto"){
                          swal("¡" + response + " con éxito!", "Se ha guardado con exito la inscripcion :)", "success");
                         }
                         $('.paginita').load('/inscripcionManual');
                    },
                    error:function(response){
                         swal("Ocurrió un error inesperado :(" , "Error");
                    }
                });
        
                $.ajax({
                    method: 'POST',
                    url: '/guardarInscripcionAsignatura/', // holi
                    data: {
                            listaAsignaturas: listaAsignaturas,
                    },
                    success:function(response){
                         //this gets called when server returns an OK response
                         if(response == "correcto"){
                          swal("¡" + response + " con éxito!", "Se ha guardado con exito la inscripcion :)", "success");
                         }
                         $('.paginita').load('/inscripcionManual');
                    },
                    error:function(response){
                         swal("Ocurrió un error inesperado :(" , "Error");
                    }
                });
            } else {
              swal("Your imaginary file is safe!");
            }
          });

        
        
        

    });
    
});