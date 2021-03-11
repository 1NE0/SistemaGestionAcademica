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
  
  

/* TODO SOBRE EL CRUD */

$(function() {
  $('.acc-btn').click(function(){
    if ( $(this).next().is( ":hidden" ) ) {
      $('.acc-content').slideUp('selected');
      $(this).next().slideDown('selected');
    } else {
      $(this).next().slideUp('selected');
    };

    
  
});


    var buttonpressed; 
       ///////////////////////////////////////////////////////////
       $('.enviar').click(function() {  
             buttonpressed = $(this).attr('name')
       })
       $('#formCrearCurso').on('submit', function(e) {
           console.log("me envie");
           e.preventDefault();
           var inputs = $("#formCrearCurso :input").serializeArray();
            console.log(inputs);
          
        
            $.ajax({
            type: "POST",
            url: $("#formCrearCurso").attr("action"),
            data: {
                csrfmiddlewaretoken:inputs[0].value,
                cod_curso: inputs[1].value,
                nom_curso: inputs[2].value,
                nivel: inputs[3].value,
                descripcion: inputs[4].value,
                docente: inputs[5].value,
                grupo: inputs[6].value,
                dia: inputs[7].value,
                hora_inicial: inputs[8].value,
                hora_final: inputs[9].value
            },
            dataType: "html",
            beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                // antes de enviar la peticion
                console.log(" esperando...");
            },
            success: function (response) {
                if(response == "correcto"){
                    swal("Correcto!", "El curso se ha registrado con éxito.", "success");
                    $('.contenido').parents('.contenedor-central').load('/cursos');
                }
                console.log(response);
            },
            error: function (response) {
                
                console.log(response)
            }
        });
    
       })
    });


// GUARDAR PROGRAMA
$(this).children('span').hide();
$('.botonGuardar').click(function(e){
  e.preventDefault();
  $(this).addClass("text-nowrap");
  $(this).children('span').show();
  var codigoPrograma = $(this).attr('id');
  // que hacer despues de hacer click en guardar
  var listaCursos = [];
  console.log($(this).siblings('.example-dropzone').attr('class'));

  $(this).siblings('.example-dropzone').children('.example-draggable').each(function(){  // recorrer los hijos del dropzone, que en este caso son los cursos
    listaCursos.push($(this).attr('id'));  // los guardamos en la lista antes creada
  });

  // mandarlos a la vista
  $.ajax({
    type: "POST",
    url: '/guardarCursoPrograma/',
    data: {
        listaCursos : listaCursos,
        programa: codigoPrograma,
    },
    dataType: "html",
    beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
        // antes de enviar la peticion
        console.log("realizando envio de cursos...");
    },
    success: function (response) {
        if(response == 'Perfecto'){
            swal("Correcto!", "El programa se ha guardado con éxito.", "success");
            $('.principal').load('/asignaturas');
        }

        $('.contenido').parents('.contenedor-central').load('/cursos');
        
    },
    error: function (response) {
        console.log(response)
    }
  }); 


});

// Abrir modal creacion
function abrirModal(url , identificacion){
  jQuery.noConflict();
    $('#creacion').load(url, function(){ // cargar el html en el modal con el parametro
      $(this).modal({
          backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
          keyboard: false     // evita cerrarla con esc.

      })
      $(this).modal('show');  // mostrar el modal
    });

     
   
   //return false;  
}

function cerrarModal() {
  jQuery.noConflict();  
  console.log("antes");
  $('.modal').modal('hide');
  console.log("despues");
  
  return false;
}


/*  acordion */

/* acordion */



