// AQUI ESTA LA LOGICA PARA EL DROG AND DROP


function onDragStart(event) {   // CUANDO SE COMIENZA A ARRASTRAR
    
    event
      .dataTransfer
      .setData('text/plain', event.target.id);   // AQUI POR LO QUE ENTIENDO SE ROTA EL ID DEL OBJETO DE DONDE SE ARRASTRA
  
     //cuando se empice a arrastrar el elemento
     /* event
     .currentTarget
    .style
    .backgroundColor = 'black'; */
}
  
  function onDragOver(event) {   // MIENTRAS SE ARRASTRA, PREVENIR QUE SE RECARGUE LA PAGINA
    event.preventDefault();
    event.currentTarget.style.heigth = 'auto';
  }
  
  function onDrop(event) {   // CUANDO SE SUELTE
    const id = event // EL OBJETO QUE REALIZA LA OPCION
      .dataTransfer
      .getData('text');   
    
    const draggableElement = document.getElementById(id);  // LO BUSCAMOS EN EL DOCUMENTO
    const dropzone = event.target; // EL TARGET HACE REFERENCIA A DONDE VA A SOLTAR EL ELEMENTO, OSEA EL DROPZONE = PANEL DESTINO
    dropzone.appendChild(draggableElement); // agregarle el elemento que estamos arrastrando
  
    event  // borrar la transferencia
    .dataTransfer
    .clearData();
  }









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
    $('.paginita').load('/asignaturas');
    return false;
}




$(document).ready(function(){
    
    $('#cargando').hide();
    // GUARDAR TODO
    $('.guardar').click(function(){
        $('#cargando').show();
        console.log("me dieron click ay");
        $('.carta').each(function(){
            
            programa = $(this).attr('id');
            listaInscripciones = [];
            $(this).children('.example-dropzone').children('.example-draggable').each(function(){
                listaInscripciones.push($(this).attr('id')); 
            })
            $.ajax({
                url: '/asignarAsignaturaProgramas/',  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
                type: "POST",       // MODO DE ENVIO
                data: {
                    programa : programa,
                    listaInscripciones : listaInscripciones,

                },
                dataType: "html",
    
                beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                    // antes de enviar la peticion
                },
                success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
                    swal("Registrado exitosamente :)", "Se ha registrado correctamente todas las asignaturas", "success");
                    $('#cargando').hide();
                    console.log("reealizando...");
                    console.log(response);
                },
                error: function (response) {
                    
                    // si todo sale mal
                    console.log(response)
                    e.preventDefault();
                },
            });
        })
        
    });


    $('.acc-btn').click(function(){
        if ( $(this).next().is( ":hidden" ) ) {
            $('.acc-content').slideUp('selected');
            $(this).next().slideDown('selected');
        } else {
            $(this).next().slideUp('selected');
        };
    });

    $('#formCrear').on("submit", function(e) {
        e.preventDefault();

        var data = $("#formCrear :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
        console.log(data);
        console.log("estoy en form crear");
            $.ajax({
                url: $("#formCrear").attr("action"),  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
                type: "POST",       // MODO DE ENVIO
                data: {
                    csrfmiddlewaretoken: data[0].value,  // QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
                    codigo: data[1].value,
                    nombre: data[2].value,
                    descripcion: data[3].value,
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

    $('#formEditarAsignatura').on("submit", function(e) {
        e.preventDefault();
        console.log("estoy en form editar");
        var data = $("#formEditarAsignatura :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
        console.log(data);

            $.ajax({
                url: $("#formEditarAsignatura").attr("action"),  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
                type: "POST",       // MODO DE ENVIO
                data: {
                    csrfmiddlewaretoken: data[0].value,  // QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
                    asignaturaSelect : data[1].value,
                    nivel: data[2].value,
                    descripcion: data[3].value,
                    dia: data[4].value,
                    hora_inicial: data[5].value,
                    hora_final: data[6].value,
                    docente: data[7].value,
                },
                dataType: "html",

                beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                    // antes de enviar la peticion
                    console.log("reealizando...");

                },
                success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
                        if(response == "correcto"){
                            swal("Registrado exitosamente :)", "Se ha registrado correctamente el nivel de la asignatura", "success");
                            
                        }else if(response == "nivelRepetido"){
                            swal("Ocurrió un error :(", "Ya hay una asignatura con este nivel", "error");
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