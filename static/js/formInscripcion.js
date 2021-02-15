$(document).ready(function(){
    $(".form-wrapper .button").click(function(){
      var boton = $(this);
      var sectionActivo = boton.parents('.section');
      var headerActivo = $(".steps .is-active");
      var headerSiguiente = headerActivo.parents('a').next().children('li');

      sectionActivo.removeClass("is-active").next().addClass("is-active");
      headerActivo.removeClass("is-active");
      headerSiguiente.addClass("is-active");


    });

    $(".steps a").click(function(e){
        var ancla = $(this); 
        $(".steps .is-active").removeClass("is-active");  // remover el anterior activo
        ancla.children('li').addClass("is-active");         // poner el que se presiono como activo

        var header = ancla.children('li').attr('id');
        
        //$(".form-wrapper .is-active").removeClass("is-active");
        $("fieldset").removeClass("is-active");
        $("#section" + header).addClass("is-active");

    });

    /* envio de formulario  */
    $(".form-wrapper").submit(function(e) {
        e.preventDefault();
        console.log("me envie");
        var data = $("#inscripcionForm :input").serializeArray();
        console.log(data);
          $.ajax({
            method: 'POST',
            url: '/registrarInscripcion/',  // la url a la cual irá la peticion
            data: {
                    csrfmiddlewaretoken: data[0].value,
                    tipoDocumento: data[1].value,   // parametros que se le mandaran a la vista
                    identificacion: data[2].value,
                    nombres: data[3].value,
                    apellidos: data[4].value,
                    edad: data[5].value,
                    genero: data[6].value,
                    programa: data[7].value,
                    departamento: data[8].value,
                    ciudad: data[9].value,
                    direccion: data[10].value,
                    telefono: data[11].value,
                    correo: data[12].value,
                    username: data[13].value,
                    password: data[14].value,
                    password2: data[15].value,
        
            },
            success:function(response){
                //     SINO SALE NINGUN ERROR
                if(response == "Incorrecto"){
                  swal("Ha ocurrido un error :(" , "El programa al que se quiere registrar el estudiante, no está disponible en este periodo" , "error");
                }else if(response == "Username ya usado"){
                  swal("Ha ocurrido un error :(" , "El username ya se encuentra ocupado, por favor utilice otro" , "error");
                }else{
                  swal("¡se realizó con exito la acción!", {
                    icon: "success",
                  });

                  window.location = "/home";
                }
                
            },
            error:function(response){
                swal("Ocurrió un error inesperado :(" , "error");
            }
        });
      });

  });
  