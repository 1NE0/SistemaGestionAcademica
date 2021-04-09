// obtener el formulario
const formulario = document.getElementById('form_periodos');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#form_periodos input');

var fechaI = false;
var fechaF = false;


const validarFormulario = (e) => {
    const fechaActual = new Date();
    
    switch(e.target.name){
         case "trip-start-inicio":
             console.log('funciona')
            //  este es el valor que obtenemos en  el input
             var fechas = document.getElementById('start_Finicio').value
            //se transforma a un date 
             var fechaprueba = new Date(fechas);
             //se le suma un dia por que segun como se edite el input queda un dia menos
             fechaprueba.setDate(fechaprueba.getDate()+1);

             if(fechaprueba < fechaActual){
                 console.log('fecha menor');
                 document.querySelector('#inicio .fomulario__input-error').classList.add('fomulario__input-error-activo')
                 document.getElementById('inicio').classList.remove('grupo-correcto')
                 document.getElementById('inicio').classList.add('grupo-incorrecto')
                 fechaI = false;

             }else{
                document.querySelector('#inicio .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('inicio').classList.add('grupo-correcto')
                document.getElementById('inicio').classList.remove('grupo-incorrecto')
                fechaI = true;

                 console.log('fecha mayor');
             }
           
            
            //  console.log(fechas);
             console.log('fecha actual' + fechaActual);
             console.log('fecha de prubea:' + fechaprueba.toLocaleDateString());
             
            
         break;
         case "trip-start-final":
             var fechainput = document.getElementById('start_Ffinal').value
             var fechaFinal = new Date(fechainput);
             fechaFinal.setDate(fechaFinal.getDate()+1)

             var fechas = document.getElementById('start_Finicio').value
              var fechaprueba = new Date(fechas);
              fechaprueba.setDate(fechaprueba.getDate()+1);

             console.log(fechainput + '\n' + fechaFinal);

             if(fechaFinal <= fechaprueba){
                document.querySelector('#final .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('final').classList.remove('grupo-correcto')
                document.getElementById('final').classList.add('grupo-incorrecto')
                fechaF = false;
                 console.log('error fecha final');
             }else{
                document.querySelector('#final .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('final').classList.add('grupo-correcto')
                document.getElementById('final').classList.remove('grupo-incorrecto')
                fechaF = true;

                console.log('exicto fecha final');

             }
            
            
            
            
        break;
             
    }

    const boton = document.getElementById('btn_crearP');
    if(fechaI ==false || fechaF == false ){
            // botonRegistrar.attr("disabled", true);
            boton.disabled=true;
            console.log('hay un campo malo ')
        }else{
            console.log('todos estan buenos ');
            boton.disabled=false;
        }  

}


  








// realiza la validacion en los inputs
inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
    
});