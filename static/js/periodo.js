$(document).ready(function () {
  $("#form_periodos").on("submit", function (e) {
    //use on if jQuery 1.7+
    e.preventDefault(); //prevent form from submitting
    var data = $("#form_periodos :input").serializeArray();
    console.log(data); // use the console for debugging, F12 in Chrome, not alerts
    $.ajax({
      url: "/periodos/",
      type: "POST",
      data: {
        csrfmiddlewaretoken: data[0].value,
        Fecha_inicio: data[1],
        Fecha_final: data[2],
      },
      dataType: "html",
      beforeSend: function(){
          console.log("reealizando...");
      },
      error: function (response) {
        e.preventDefault();
      },
    });
  });
});

