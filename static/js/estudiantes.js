
$(document).ready(function () {
  $("#input_nombre").keyup(function () {
    _this = this;
    // Muestra solo los TR, oculta el resto de ellos
    $.each($("#tabla tbody tr"), function () {
      if ($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) // si la fila contiene algun caracter del input
        $(this).hide(); // ocultar
      else 
        $(this).show();  // mostrar
    });
  });                     
});

// $(document).ready(function () {
//   $("#botoncito").on("click", function (e) {
//     // cuando se haga click en el boton con ID "botoncito"
//     e.preventDefault(); // no recargue la pagina
//     nombre_input = $("#input_nombre").val(); // obtener el valor que se ingreso en el input con ID "input_nombre"
//     $.ajax({
//       url: "/buscarestudiante/", // a que vista va a pedir los datos
//       type: "GET", // con que método se pediran
//       data: {
//         nombre: nombre_input, //el valor define lo que se va a colocar en la URL ejemplo : /buscarestudiante/?nombre=
//       }, // lo que le asignamos es el nombre que acaba de dar el usuario en el input
//       dataType: "json", // como lo va a mostrar, como un json
//       success: function (response) {
//         // si se hace todo bien, devolverá un objeto "response" que es el arreglo
//         console.log(response[0].fields.nombres); // sacamos del json lo que necesitamos
//         console.log(response[0].fields.apellidos);

//         // poner en la tabla
//       },
//       error: function (error) {
//         console.log(error);
//       },
//     });

//     // ignorar
//     return false;
//     console.log("holi");
//   });
// });