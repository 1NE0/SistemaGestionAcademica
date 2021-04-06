
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
          swal("¡Bien hecho!", "Se Guardó con exito el documento :)", "success");
          $('.contenedor').load('/asignaturasDocente');
        }
    },
    error: function (response) {
        // si todo sale mal
    },
    });
});

// logica de eliminar
$('.eliminar').click(function(){
  var codigoActividad = $(this).attr('id');
  var codigo = [];
  codigo.push(codigoActividad);
  $.ajax({
    type: "POST",
    url: '/eliminarActividad/',
    data: {
      codActividad : codigo,
    },
    success: function(response) {
      if (response == "correcto") {
        swal("¡Bien hecho!", "Se eliminó con exito el documento", "success");
        $('.contenedor').load('/asignaturasDocente');
      } else {
        alert('Ocurrió un error mientras se eliminaba el archivo');
      }
    }
  })

});


/* ESTILO CSS Y JS */
// Also see: https://www.quirksmode.org/dom/inputfile.html

var inputs = document.querySelectorAll('.file-input')

for (var i = 0, len = inputs.length; i < len; i++) {
  customInput(inputs[i])
}

function customInput (el) {
  const fileInput = el.querySelector('[type="file"]')
  const label = el.querySelector('[data-js-label]')
  
  fileInput.onchange =
  fileInput.onmouseout = function () {
    if (!fileInput.value) return
    
    var value = fileInput.value.replace(/^.*[\\\/]/, '')
    el.className += ' -chosen'
    label.innerText = value
  }
}