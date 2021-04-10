


$(document).ready(function(){
    textoVerficacionId = $('.identificacionVerificada');
    textoVerficacionIdNo = $('.identificacionNoVerificada');
    botonRegistrar = $('.registrar');
    botonRegistrarOcultar = $('.NoRegistrar');

    botonRegistrarOcultar.show();
    botonRegistrar.attr("disabled", true);
    textoVerficacionIdNo.hide();
    textoVerficacionId.hide();

    $('.cursoMusica').hide();



    /* CURSOS DEL PROGRAMA DE MUSICA LOGICA */

    $('#comboProgramas').click(function(){
      console.log("hola");
      if($(this).val() == "musica" || $(this).val() == "música" || $(this).val() == "Música" || $(this).val() == "Musica" || $(this).val() == "Music"  || $(this).val() == "Musicaa"){
        $('.cursoMusica').show();
      }else{
        $('.cursoMusica').hide();
      }
    });



    $('.boton').attr("disabled", true);

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
                    cursoMusica: data[8].value,
                    departamento: data[9].value,
                    ciudad: data[10].value,
                    direccion: data[11].value,
                    telefono: data[12].value,
                    correo: data[13].value,
                    username: data[14].value,
                    password: data[15].value,
                    password2: data[16].value,
        
            },
            success:function(response){
                //     SINO SALE NINGUN ERROR
                if(response == "Incorrecto"){
                  swal("Ha ocurrido un error :(" , "El programa al que se quiere registrar el estudiante, no está disponible en este periodo" , "error");
                }else if(response == "Username ya usado"){
                  swal("Ha ocurrido un error :(" , "El username ya se encuentra ocupado, por favor utilice otro" , "error");
                }else if(response == "me la pelas"){
                  swal("Ha ocurrido un error :(" , "No se seleccionó un programita" , "error");
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


      // verificar el user
    $('.form-wrapper .username').on("blur",function() {

      var username = $(this).val();		
      var dataString = 'username='+username;

      if(username != ""){
        $.ajax({
          type: "POST",
          url: "/verificarUser/",
          data: dataString,
          dataType: "html",
          success: function(data) {
              if(data == "disponible"){
                $('.username').addClass("userVerificado");
                $('.username').removeClass("userRepetido");
                
              }else if(data == "noDisponible"){
                $('.username').addClass("userRepetido");
                $('.username').removeClass("userVerificado");
              }
          },
          error: function(data){
            console.log("error");
          }
      });
      }else{
        $('.username').removeClass("userRepetido");
        $('.username').removeClass("userVerificado");
      }
      

    });

    // verificar el user
    $('.form-wrapper .identificacion').on("blur",function() {

      var identificacion = $(this).val();		
      var dataString = 'identificacion='+identificacion;

      if(identificacion != ""){
        $.ajax({
          type: "POST",
          url: "/verificarIdentificacion/",
          data: dataString,
          dataType: "html",
          success: function(data) {
              if(data == "disponible"){
                textoVerficacionId.show();
                textoVerficacionIdNo.hide();
                $('.identificacion').addClass("userVerificado");
                $('.identificacion').removeClass("userRepetido");
              }else if(data == "noDisponible"){
                textoVerficacionId.hide();
                textoVerficacionIdNo.show();
                $('.identificacion').addClass("userRepetido");
                $('.identificacion').removeClass("userVerificado");
              }
          },
          error: function(data){
            console.log("error");
          }
      });
      }else{
        textoVerficacionIdNo.hide();
        textoVerficacionId.hide();
        $('.identificacion').removeClass("userRepetido");
        $('.identificacion').removeClass("userVerificado");
      }
      

    });

    $('fieldset input').on("keyup" , function(){
      console.log("entreee");
      var form = $('.form-wrapper');
      var check = checkCampos(form);
      if(check) {
          console.log("estan llenos");
          // habilitar boton
          botonRegistrar.attr("disabled", false);
          
      }
      else {
        botonRegistrar.attr("disabled", true);
        //deshabilitar boton
      }
    });

    //Función para comprobar los campos de texto
    function checkCampos(obj) {
      var camposRellenados = true;
      obj.find("input").each(function() {
      var $this = $(this);
          if( $this.val().length <= 0 ) {
              camposRellenados = false;
              return false;
          }
      });
      if(camposRellenados == false) {
          return false;
      }
      else {
          return true;
      }
    }
    
    

    


      
  });
  