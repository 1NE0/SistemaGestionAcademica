$(document).ready(function () {  // cuando el documento esté listo
  $("#form_periodos").on("submit", function (e) {   // coger el formulario con id "form_periodos"
    
    e.preventDefault(); // PREVENIR QUE SE RECARGUE LA PAGINA
    var data = $("#form_periodos :input").serializeArray(); // COGER SUS INPUTS, Y SERIALIZARLOS EN JSON
    console.log(data); // use the console for debugging, F12 in Chrome, not alerts
    $.ajax({
      url: "/periodos/",  // URL A LA QUE SE REALIZA LA PETICION
      type: "POST",       // MODO DE ENVIO
      data: {
        csrfmiddlewaretoken: data[0].value,  // QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
        Fecha_inicio: data[1].value,
        Fecha_final: data[2].value,
      },
      dataType: "json",
      beforeSend: function(response){
        // antes de enviar la peticion
          console.log("reealizando...");
      },
      success: function(response){
        // si todo sale bien
        console.log("hola")
        swal("Hello world!");
      },
      error: function (response) {
        // si todo sale mal
        e.preventDefault();
      },
    });
  });
});

