
var $cell = $('.card');

//open and close card when clicked on card
$cell.find('.js-expander').click(function() {

  var $thisCell = $(this).closest('.card');

  if ($thisCell.hasClass('is-collapsed')) {
    $cell.not($thisCell).removeClass('is-expanded').addClass('is-collapsed').addClass('is-inactive');
    $thisCell.removeClass('is-collapsed').addClass('is-expanded');
    
    if ($cell.not($thisCell).hasClass('is-inactive')) {
      //do nothing
    } else {
      $cell.not($thisCell).addClass('is-inactive');
    }

  } else {
    $thisCell.removeClass('is-expanded').addClass('is-collapsed');
    $cell.not($thisCell).removeClass('is-inactive');
  }
});

//close card when click on cross
$cell.find('.js-collapser').click(function() {

  var $thisCell = $(this).closest('.card');

  $thisCell.removeClass('is-expanded').addClass('is-collapsed');
  $cell.not($thisCell).removeClass('is-inactive');

});


$('#form').submit(function(e){
  e.preventDefault(); // PREVENIR QUE SE RECARGUE LA PAGINA
  var formData = new FormData(this);
  console.log(formData); // use the console for debugging, F12 in Chrome, not alerts
  $.ajax({
    url: $(this).attr("action"),  // URL A LA QUE SE REALIZA LA PETICION DEL FORM
    type: "POST",       // MODO DE ENVIO
    data:formData,// QUE ATRIBUTOS MANDAMOS A LA VISTA O PETICION
    processData: false,
    contentType: false,
    dataType: "html",
    beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
        // antes de enviar la peticion
        console.log("reealizando...");
    },
    success: function(response){    // AL TERMINAR SATISFACTORIAMENTE
        if(response == "correcto"){
          swal("¡Bien hecho!", "Se registro con exito", "success");
          $('body').load('/asignaturasDocente');
        }
    },
    error: function (response) {
        // si todo sale mal
    },
    });
});