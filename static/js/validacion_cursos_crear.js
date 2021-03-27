// obtener el formulario
const formulario = document.getElementById('formCrearCurso');
//obtener todos los inputs del fromulario
const inputs = document.querySelectorAll('#formCrearCurso input');
// obtener el formulario
const formularioedit = document.getElementById('formEditarCurso');
//obtener todos los inputs del fromulario
const inputsedit = document.querySelectorAll('#formEditarCurso input');


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
        case "cod_curso":
            console.log('entre a codigo')
            if(expresiones.codigo.test(e.target.value)){
                document.getElementById('codigo').classList.add('grupo-correcto')
                document.getElementById('codigo').classList.remove('grupo-incorrecto')
                document.querySelector('#codigo .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.getElementById('codigo').classList.remove('grupo-correcto')
                document.getElementById('codigo').classList.add('grupo-incorrecto')
                document.querySelector('#codigo .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }

        break;
        case "nom_curso":
            console.log('entre a nombre')
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('nombre').classList.add('grupo-correcto')
                document.getElementById('nombre').classList.remove('grupo-incorrecto')
                document.querySelector('#nombre .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.getElementById('nombre').classList.remove('grupo-correcto')
                document.getElementById('nombre').classList.add('grupo-incorrecto')
                document.querySelector('#nombre .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }

        break;
        case "descripcion":
            console.log('entre a descripcion')
            if(expresiones.descripcion.test(e.target.value)){
                document.getElementById('descripcion').classList.add('grupo-correcto')
                document.getElementById('descripcion').classList.remove('grupo-incorrecto')
                document.querySelector('#descripcion .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.getElementById('descripcion').classList.remove('grupo-correcto')
                document.getElementById('descripcion').classList.add('grupo-incorrecto')
                document.querySelector('#descripcion .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }

        break;
        case "grupo":
            console.log('entre a grupo')
            if(expresiones.grupo.test(e.target.value)){
                document.getElementById('grupo').classList.add('grupo-correcto')
                document.getElementById('grupo').classList.remove('grupo-incorrecto')
                document.querySelector('#grupo .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.getElementById('grupo').classList.remove('grupo-correcto')
                document.getElementById('grupo').classList.add('grupo-incorrecto')
                document.querySelector('#grupo .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }

        break;
        case "hora_inicial":
            //trae la hora como 18:00 o 6:00 <string>
            var hor = document.getElementById('appt_inicio').value
            console.log(hor)
            
            if(hor > "18:00" || hor < "08:00"){
                console.log('hora salida')
                document.querySelector('#hora_inicial .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('hora_inicial').classList.remove('grupo-correcto')
                document.getElementById('hora_inicial').classList.add('grupo-incorrecto')

            }else{
                document.querySelector('#hora_inicial .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('hora_inicial').classList.add('grupo-correcto')
                document.getElementById('hora_inicial').classList.remove('grupo-incorrecto')
            }
        break;     
        case "hora_final":
            // trae la hora como 18:00 o 6:00 <string>
            var hor = document.getElementById('appt_inicio').value
            console.log(hor)
            var horaF = document.getElementById('appt_final').value
             console.log(horaF)
            
            if(horaF < hor || horaF > "18:00"){
                console.log('hora horafinal')
                document.querySelector('#hora_final .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('hora_final').classList.remove('grupo-correcto')
                document.getElementById('hora_final').classList.add('grupo-incorrecto')

            }else{
                document.querySelector('#hora_final .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('hora_final').classList.add('grupo-correcto')
                document.getElementById('hora_final').classList.remove('grupo-incorrecto')
            }
        break;   
            

    }
}

//para formulario de editar

const validarFormularioedid = (e) => {
    switch(e.target.name){
        case "descripcion":
            console.log('entre a descripcion edidtar')
            if(expresiones.descripcion.test(e.target.value)){
                 document.getElementById('descripcionedid').classList.add('grupo-correcto')
                 document.getElementById('descripcionedid').classList.remove('grupo-incorrecto')
                document.querySelector('#descripcionedid .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                 document.getElementById('descripcionedid').classList.remove('grupo-correcto')
                 document.getElementById('descripcionedid').classList.add('grupo-incorrecto')
                document.querySelector('#descripcionedid .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }
            break;
            case "grupo":
            console.log('entre a grupo editar')
            if(expresiones.grupo.test(e.target.value)){
                document.getElementById('grupo_editar').classList.add('grupo-correcto')
                document.getElementById('grupo_editar').classList.remove('grupo-incorrecto')
                document.querySelector('#grupo_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')

            }else{
                document.getElementById('grupo_editar').classList.remove('grupo-correcto')
                document.getElementById('grupo_editar').classList.add('grupo-incorrecto')
                document.querySelector('#grupo_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')

            }

        break;
        case "hora_inicial":
            //trae la hora como 18:00 o 6:00 <string>
            var hor = document.getElementById('appt_inicio_editar').value
            console.log(hor)
            
            if(hor > "18:00" || hor < "08:00"){
                console.log('hora salida')
                document.querySelector('#hora_inicial_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('hora_inicial_editar').classList.remove('grupo-correcto')
                document.getElementById('hora_inicial_editar').classList.add('grupo-incorrecto')

            }else{
                document.querySelector('#hora_inicial_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('hora_inicial_editar').classList.add('grupo-correcto')
                document.getElementById('hora_inicial_editar').classList.remove('grupo-incorrecto')
            }
        break;
        case "hora_final":
            // trae la hora como 18:00 o 6:00 <string>
            var hor = document.getElementById('appt_inicio_editar').value
            console.log(hor)
            var horaF = document.getElementById('appt_final_editar').value
             console.log(horaF)
            
            if(horaF <= hor || horaF > "18:00"){
                console.log('hora horafinal')
                document.querySelector('#hora_final_editar .fomulario__input-error').classList.add('fomulario__input-error-activo')
                document.getElementById('hora_final_editar').classList.remove('grupo-correcto')
                document.getElementById('hora_final_editar').classList.add('grupo-incorrecto')

            }else{
                document.querySelector('#hora_final_editar .fomulario__input-error').classList.remove('fomulario__input-error-activo')
                document.getElementById('hora_final_editar').classList.add('grupo-correcto')
                document.getElementById('hora_final_editar').classList.remove('grupo-incorrecto')
            }
        break;   
    }

}




inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
    input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
});
inputsedit.forEach((input1)=>{
    input1.addEventListener('keyup', validarFormularioedid); //valida cuando se levanta la tecla
    input1.addEventListener('blur', validarFormularioedid);  //valida cuando se hace clik en otro lado
});