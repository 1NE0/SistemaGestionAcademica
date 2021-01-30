
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
    console.log("hola");
    $('#creacion').modal('hide');
    return false;
  }

  $(function(){

    var buttonpressed;
    $('.crear').click(function(){
      buttonpressed = $(this).attr('name')
    })
    $('#form_programas').on('submit',function(e){
        e.preventDefault();
        var data = $("#form_programas :input").serializeArray();

        $.ajax({
          url : $(this).attr('action'),
          type: "POST",
          data: {
            csrfmiddlewaretoken: data[0].value,
            cod_programa: data[1].value,
            nom_programa: data[2].value,
            contenido_Aca: data[3].value
          },
          dataType: "json",
          beforeSend: function(response){
            console.log("realizando..");
          },
          success: function(response){
            agregarFila(response['cod_programa'],response['nom_programa'],response['contenido_Aca']);
          },
          error: function(response){
            console.log(response)
            e.preventDefault();
          },
        });

    })

  })

function agregarFila(cod_programa,nom_programa,contenido_Aca){
    var htmlTags = '<tr style="color:white;font-weight:bold;background-color:#092638;">'+
                      '<td>' + cod_programa + '</td>'+
                      '<td>' + nom_programa + '</td>'+
                      '<td>' + contenido_Aca + '</td>'
                  '</tr>'
    $('#tabla tbody').append(htmlTags);
    console.log("actulizacion")
}

