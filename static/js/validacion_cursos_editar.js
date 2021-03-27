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



// inputs.forEach((input)=>{
//     input.addEventListener('keyup', validarFormulario); //valida cuando se levanta la tecla
//     input.addEventListener('blur', validarFormulario);  //valida cuando se hace clik en otro lado
// });