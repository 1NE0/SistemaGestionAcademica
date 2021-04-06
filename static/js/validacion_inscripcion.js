// obtener el formulario
const formulario = document.getElementById('inscripcionForm');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#inscripcionForm input');


const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/, // 7 a 14 numeros.
    edad: /^\d{1,2}$/
    

}


    var identificaion= false;
    var nombres= false;
    var apellidos= false;
    var edad= false;
    var telefono= false;
    var correo= false;
    var usuario=false;
    var contraseña1=false;
    var contraseña2=false;


 
const validarFormulario = (e) => {
    switch(e.target.name){
        case "identificacion":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('identificacion').classList.add('grupo-correcto')
                document.getElementById('identificacion').classList.remove('grupo-incorrecto')
                document.querySelector('#identificacion .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                identificaion=true;
            }else{
                document.querySelector('#identificacion .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('identificacion').classList.remove('grupo-correcto')
                document.getElementById('identificacion').classList.add('grupo-incorrecto')
                identificaion=false;
            }

        break;
        case "nombres":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#nombre .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('nombre').classList.remove('grupo-incorrecto')
                document.getElementById('nombre').classList.add('grupo-correcto')
                nombres=true;
            }else{
                document.getElementById('nombre').classList.add('grupo-incorrecto')
                document.querySelector('#nombre .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('nombre').classList.remove('grupo-correcto')
                nombres=false;
            }

        break;
        case "apellidos":
            console.log('funciona');
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('apellido').classList.add('grupo-correcto')
                document.getElementById('apellido').classList.remove('grupo-incorrecto')
                document.querySelector('#apellido .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                apellidos=true;
            }else{
                document.querySelector('#apellido .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('apellido').classList.remove('grupo-correcto')
                document.getElementById('apellido').classList.add('grupo-incorrecto')
                apellidos=false;
            }
            

        break;
        case "edad":
            console.log('funciona');
            if(expresiones.edad.test(e.target.value)){
                document.getElementById('edad').classList.add('grupo-correcto')
                document.getElementById('edad').classList.remove('grupo-incorrecto')
                document.querySelector('#edad .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                edad=true;
            }else{
                document.querySelector('#edad .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('edad').classList.remove('grupo-correcto')
                document.getElementById('edad').classList.add('grupo-incorrecto')
                edad=false;
            }
            

        break;
        case "telefono":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('telefono').classList.add('grupo-correcto')
                document.getElementById('telefono').classList.remove('grupo-incorrecto')
                document.querySelector('#telefono .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                telefono=true;
            }else{
                document.querySelector('#telefono .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('telefono').classList.remove('grupo-correcto')
                document.getElementById('telefono').classList.add('grupo-incorrecto')
                telefono=false;
            }
            

        break;
        case "correo":
            console.log('funciona');
            if(expresiones.correo.test(e.target.value)){
                document.getElementById('email').classList.add('grupo-correcto')
                document.getElementById('email').classList.remove('grupo-incorrecto')
                document.querySelector('#email .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                correo=true;
            }else{
                document.querySelector('#email .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('email').classList.remove('grupo-correcto')
                document.getElementById('email').classList.add('grupo-incorrecto')
                correo=false;
            }
            

        break;
        case "username":
            console.log('funciona');
            if(expresiones.usuario.test(e.target.value)){
                document.getElementById('usuario').classList.add('grupo-correcto')
                document.getElementById('usuario').classList.remove('grupo-incorrecto')
                document.querySelector('#usuario .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                usuario=true;
            }else{
                document.querySelector('#usuario .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('usuario').classList.remove('grupo-correcto')
                document.getElementById('usuario').classList.add('grupo-incorrecto')
                usuario=false;
            }
            

        break;
        case "password":
            console.log('funciona');
            if(expresiones.usuario.test(e.target.value)){
                document.getElementById('contraseña').classList.add('grupo-correcto')
                document.getElementById('contraseña').classList.remove('grupo-incorrecto')
                document.querySelector('#contraseña .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                contraseña1=true;
            }else{
                document.querySelector('#contraseña .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('contraseña').classList.remove('grupo-correcto')
                document.getElementById('contraseña').classList.add('grupo-incorrecto')
                contraseña1=false;

            }
            

        break;
        case "password2":
                const inputPassword1 = document.getElementById('password');
	            const inputPassword2 = document.getElementById('password2');
                console.log('funciona');
            if(inputPassword1.value == inputPassword2.value){
                document.getElementById('contraseña2').classList.add('grupo-correcto')
                document.getElementById('contraseña2').classList.remove('grupo-incorrecto')
                document.querySelector('#contraseña2 .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                contraseña2=true;
            }else{
                document.querySelector('#contraseña2 .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('contraseña2').classList.remove('grupo-correcto')
                document.getElementById('contraseña2').classList.add('grupo-incorrecto')
                contraseña2=false;
            }
            

        break;
        
    }

    const boton = document.getElementById('btn_registrar');
    if(identificaion ==false || nombres == false || apellidos==false || edad== false || telefono == false || correo== false
        || usuario==false || contraseña1==false || contraseña2==false ){
            // botonRegistrar.attr("disabled", true);
            boton.disabled=true;
            console.log('hay un campo malo ')
        }else{
            console.log('todos estan buenos ');
            boton.disabled=false;
        }  

    

}

//boton balidar//
// const validarbtn = (e) => {

    
//     if(campos.identificaion && campos.nombres && campos.apellidos && campos.edad && campos.telefono && campos.correo
//         && campos.usuario && campos.contraseña1 && campos.contraseña2){
//             document.getElementById('btn_registrar').attributes.add("disabled",true)
//         }else{
//             document.getElementById('btn_registrar').attributes("disabled", false);
//             // document.getElementById("btn_registrar").disabled = true;
//         }
// };

inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
});