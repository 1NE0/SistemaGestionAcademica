// obtener el formulario
const formulario = document.getElementById('formCrearDocente');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#formCrearDocente input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/, // 7 a 14 numeros.
    edad: /^\d{1,2}$/,
    descripcion: /^[a-zA-Z0-ZÀ-ÿ-9\_\-\,\.\s]{8,60}$/,
    codigo: /^[a-zA-Z0-9\_\-]{4,8}$/,
    grupo:/^\d{1,2}$/
    

}


const validarFormulario = (e) => {
    switch(e.target.name){
        case "id":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('crear_identificacion').classList.add('grupo-correcto')
                document.getElementById('crear_identificacion').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_identificacion .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                
            }else{
                document.querySelector('#crear_identificacion .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_identificacion').classList.remove('grupo-correcto')
                document.getElementById('crear_identificacion').classList.add('grupo-incorrecto')
            }
        break;
        case "nombres":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#crear_nombres .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('crear_nombres').classList.remove('grupo-incorrecto')
                document.getElementById('crear_nombres').classList.add('grupo-correcto')
            }else{
                document.getElementById('crear_nombres').classList.add('grupo-incorrecto')
                document.querySelector('#crear_nombres .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_nombres').classList.remove('grupo-correcto')
            }

        break;
        case "apellidos":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#crear_apellidos .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('crear_apellidos').classList.remove('grupo-incorrecto')
                document.getElementById('crear_apellidos').classList.add('grupo-correcto')
            }else{
                document.getElementById('crear_apellidos').classList.add('grupo-incorrecto')
                document.querySelector('#crear_apellidos .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_apellidos').classList.remove('grupo-correcto')
            }

        break;
        case "edad":
            console.log('funciona');
            if(expresiones.edad.test(e.target.value)){
                document.getElementById('crear_edad').classList.add('grupo-correcto')
                document.getElementById('crear_edad').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_edad .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.querySelector('#crear_edad .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_edad').classList.remove('grupo-correcto')
                document.getElementById('crear_edad').classList.add('grupo-incorrecto')
            }
            

        break;
        case "telefono":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('crear_telefono').classList.add('grupo-correcto')
                document.getElementById('crear_telefono').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_telefono .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.querySelector('#crear_telefono .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_telefono').classList.remove('grupo-correcto')
                document.getElementById('crear_telefono').classList.add('grupo-incorrecto')
            }
            

        break;
        case "correo":
            console.log('entre a correo');
            if(expresiones.correo.test(e.target.value)){
                document.getElementById('crear_email').classList.add('grupo-correcto')
                document.getElementById('crear_email').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_email .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.querySelector('#crear_email .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_email').classList.remove('grupo-correcto')
                document.getElementById('crear_email').classList.add('grupo-incorrecto')
            }
            

        break;
        case "username":
            console.log('funciona');
            if(expresiones.usuario.test(e.target.value)){
                document.getElementById('crear_usuario').classList.add('grupo-correcto')
                document.getElementById('crear_usuario').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_usuario .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.querySelector('#crear_usuario .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_usuario').classList.remove('grupo-correcto')
                document.getElementById('crear_usuario').classList.add('grupo-incorrecto')
            }
            

        break;
        case "password":
            console.log('funciona');
            if(expresiones.usuario.test(e.target.value)){
                document.getElementById('crear_password').classList.add('grupo-correcto')
                document.getElementById('crear_password').classList.remove('grupo-incorrecto')
                document.querySelector('#crear_password .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.querySelector('#crear_password .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('crear_password').classList.remove('grupo-correcto')
                document.getElementById('crear_password').classList.add('grupo-incorrecto')
            }
            

        break;
       
       

    }}





inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
});