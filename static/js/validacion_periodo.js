// obtener el formulario
const formulario = document.getElementById('form_periodos');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#form_periodos input');


const validarFormulario = (e) => {
    const fechaActual = new Date().toLocaleString();
    
    switch(e.target.name){
         case "trip-start-inicio":
             console.log('funciona')
             var fecha = new Date(document.getElementById('Finicio'));
            //  var fecha2 = document.querySelector('input[type="date"]');
            //  var fecha3 = new Date(fecha2);
            //  var fecha3 = document.querySelector('#inicio .Finicio').value;
            // document.getElementById('Finicio').addEventListener('change', function() {
                      // se ejecuta cuando el datepicker cambie de valor
                    //    var input_date = this.value;
                    //    console.log(input_date)
            // })
             
             
             
              console.log(fecha.toISOString);
            //  console.log(fecha2);
            //  console.log(fecha3.getdate);
            //  console.log(fechaActual);
            //  console.log
         break;
         case "trip-start-final":
            
            
            // var fecha = new Date(document.getElementById('Ffinal').;
            
            //         var input_date = this.value;
            //         console.log(input_date)
            //     }
        break;
             
    }

}

// function modoElegirFecha() {
//     document.getElementById('start').addEventListener('change', function() {
//         // se ejecuta cuando el datepicker cambie de valor
//         var input_date = this.value;
//         console.log(input_date)
//     //     var now = new Date();
//     //     var date_selected = new Date(input_date);
//     //     if (now > date_selected) { 
//     //         alert('Invalido la fecha actual es: '+ now  + ' fecha seleccionada es: ' + date_selected) 
//     //     }
//     //     else { 
//     //         alert('la fecha:'+ input_date + ' es valida');
//     //     }
//     // });
//   }
  








// realiza la validacion en los inputs
inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
    
});