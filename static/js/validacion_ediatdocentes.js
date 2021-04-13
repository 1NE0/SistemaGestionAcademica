/* 
// obtener el formulario
const formularioeditar = document.getElementById('formEditardocente');
//obtener todos los inputs del fromulario
const inputs_editar = document.querySelectorAll('#formEditardocente input');

const expresiones_editar = {
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

var identificaion_editar = false;
    var nombres_editar= false;
    var apellidos_editar= false;
    var edad_editar=false;
    var telefono_editar= false;


const validarFormulario_editar = (e) => {
    switch(e.target.name){
        case "identificacion":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('identificacion_editar').classList.add('grupo-correcto')
                document.getElementById('identificacion_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#identificacion_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                identificaion_editar = true;
            }else{
                document.querySelector('#identificacion_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('identificacion_editar').classList.remove('grupo-correcto')
                document.getElementById('identificacion_editar').classList.add('grupo-incorrecto')
                identificaion_editar=false;
            }
        break;
        case "nombres":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#nombre_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('nombre_editar').classList.remove('grupo-incorrecto')
                document.getElementById('nombre_editar').classList.add('grupo-correcto')
                nombres_editar=true;
            }else{
                document.getElementById('nombre_editar').classList.add('grupo-incorrecto')
                document.querySelector('#nombre_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('nombre_editar').classList.remove('grupo-correcto')
                nombres_editar=false;
            }
            break;
            case "apellidos":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#apellido_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('apellido_editar').classList.remove('grupo-incorrecto')
                document.getElementById('apellido_editar').classList.add('grupo-correcto')
                apellidos_editar=true;
            }else{
                document.getElementById('apellido_editar').classList.add('grupo-incorrecto')
                document.querySelector('#apellido_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('apellido_editar').classList.remove('grupo-correcto')
                apellidos_editar=false;
            }

        break;
        case "edad":
            console.log('funciona');
            if(expresiones.edad.test(e.target.value)){
                document.getElementById('edad_editar').classList.add('grupo-correcto')
                document.getElementById('edad_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#edad_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                 edad_editar=true;
            }else{
                document.querySelector('#edad_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('edad_editar').classList.remove('grupo-correcto')
                document.getElementById('edad_editar').classList.add('grupo-incorrecto')
                 edad_editar=false;
            }
            

        break;
        case "telefono":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('telefono_editar').classList.add('grupo-correcto')
                document.getElementById('telefono_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#telefono_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                telefono_editar=true;
            }else{
                document.querySelector('#telefono_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('telefono_editar').classList.remove('grupo-correcto')
                document.getElementById('telefono_editar').classList.add('grupo-incorrecto')
                telefono_editar=false;
            }
            

        break;



    }

    const boton = document.getElementById('btn_confirmar');
    if(identificaion_editar ==false || nombres_editar == false || apellidos_editar==false || edad_editar== false || telefono_editar == false  ){
            // botonRegistrar.attr("disabled", true);
            boton.disabled=true;
            console.log('hay un campo malo ')
        }else{
            console.log('todos estan buenos ');
            boton.disabled=false;
        }  
}



inputs_editar.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario_editar); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario_editar);  //valida cuando se hace clik en otro lado
}); */