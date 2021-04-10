// obtener el formulario
const formulario = document.getElementById('formEditarEstudiantes');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#formEditarEstudiantes input');


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
                document.getElementById('id_editar').classList.add('grupo-correcto')
                document.getElementById('id_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#id_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                identificaion=true;
            }else{
                document.querySelector('#id_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('id_editar').classList.remove('grupo-correcto')
                document.getElementById('id_editar').classList.add('grupo-incorrecto')
                identificaion=false;
            }

        break;
        case "nombres":
            console.log('funciona');
             if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#nom_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('nom_editar').classList.remove('grupo-incorrecto')
                document.getElementById('nom_editar').classList.add('grupo-correcto')
                nombres=true;
            }else{
                document.getElementById('nom_editar').classList.add('grupo-incorrecto')
                document.querySelector('#nom_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('nom_editar').classList.remove('grupo-correcto')
                nombres=false;
            }

        break;
        case "apellidos":
            console.log('funciona');
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('ape_editar').classList.add('grupo-correcto')
                document.getElementById('ape_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#ape_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                apellidos=true;
            }else{
                document.querySelector('#ape_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('ape_editar').classList.remove('grupo-correcto')
                document.getElementById('ape_editar').classList.add('grupo-incorrecto')
                apellidos=false;
            }
            

        break;
        case "edad":
            console.log('funciona');
            if(expresiones.edad.test(e.target.value)){
                document.getElementById('edad_editar').classList.add('grupo-correcto')
                document.getElementById('edad_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#edad_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                edad=true;
            }else{
                document.querySelector('#edad_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('edad_editar').classList.remove('grupo-correcto')
                document.getElementById('edad_editar').classList.add('grupo-incorrecto')
                edad=false;
            }
            

        break;
        case "correo":
            console.log('funciona');
            if(expresiones.correo.test(e.target.value)){
                document.getElementById('correo_editar').classList.add('grupo-correcto')
                document.getElementById('correo_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#correo_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                correo=true;
            }else{
                document.querySelector('#correo_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('correo_editar').classList.remove('grupo-correcto')
                document.getElementById('correo_editar').classList.add('grupo-incorrecto')
                correo=false;
            }
            

        break;
        case "telefono":
            console.log('funciona');
            if(expresiones.telefono.test(e.target.value)){
                document.getElementById('telef_editar').classList.add('grupo-correcto')
                document.getElementById('telef_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#telef_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                telefono=true;
            }else{
                document.querySelector('#telef_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('telef_editar').classList.remove('grupo-correcto')
                document.getElementById('telef_editar').classList.add('grupo-incorrecto')
                telefono=false;
            }
            

        break;

        }

        const boton = document.getElementById('btn_confirmar');
    if(identificaion ==false || nombres == false || apellidos==false || edad== false || telefono == false || correo== false){
            // botonRegistrar.attr("disabled", true);
            boton.disabled=true;
            console.log('hay un campo malo ')
        }else{
            console.log('todos estan buenos ');
            boton.disabled=false;
        }  

    }




    inputs.forEach((input)=>{
        input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
        input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
    });