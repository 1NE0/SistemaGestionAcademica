/*$(document).ready(function () {
   // $("#boton").on("click", function () {  
    
    $('#buscar_curso').keyup(function (e) { // KeyUp es para solicitar una petición Ajax 
                                            // cada vez que el usuario presione una tecla dentro del input
        e.preventDefault();
        var consulta = $("#buscar_curso").val();  
        console.log(consulta);
        $.ajax({
            type: "GET",
            url: "/listacursos/",
            data: {nombre: consulta},
            dataType: "json",
            success: function (response) {
                console.log("LO LOGREE")
                console.log(response[0].fields.cod_curso) 
                console.log(response[0].fields.nom_curso)

                //listarlos en una tabla
                $("#table").DataTable({
                    responsive: true,
                    autoWidth: false,   // respeta los anchos de colum que especifique
                    destroy: true,      // reiniar la tabla
                    deferRender: true,  //agiliza la carga de los datos si son muchos
                    ajax: {
                        type: "GET",
                        url: "/listacursos/",
                        data: { nombre : consulta },
                        dataSrc: "",
                    },
                    columns: [
                        {"data": "Accion"},
                        {"data": "cod_curso"},
                        {"data": "nom_curso"},
                        {"data": "Programa"} 
                    ],
                })
            },
            error: function(response) {
                console.log("ME MORI");
            }
        });
    });
});*/
//});

$(document).ready(function () {
    $("#buscar_curso").keyup(function () { 
        _this = this;
        $.each($("#table tbody tr"), function () { 
            if ($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1)
                $(this).hide();
            else
                $(this).show();
        });
    });

    $('.botoncito').on('click' , function(){
        var codigo = $(this).attr('id');
        console.log(codigo);
        
    })
});

// Abrir modal creacion
function abrirModal(url){
   jQuery.noConflict();         // hace que ignore cuando hay varias instancias de JQuery
//    $('#miModal').modal('show');
//      var url = $(this).data("#formCrearCurso");
    $('#creacion').load(url, function(){
        $(this).modal({
            backdrop: 'static', // evita cerrar la ventana dando click fuera de ella.
            keyboard: false     // evita cerrarla con esc.
    
        })
        $(this).modal('show');  // mostrar el modal
    });

    return false;  
}



function cerrarModal() {
    modalcito = $('#miModal').parents('#creacion');
    console.log(modalcito.attr('id'));
    modalcito.modal('hide');
    $('#edicion').modal('hide');
    // actualizar contenido
    $('.contenido').load('/cursos');
    return false;
}




/* TODO SOBRE EL CRUD */

$(function() {
    var buttonpressed; 
       $('.enviar').click(function() {  
             buttonpressed = $(this).attr('name')
       })
       $('#formCrearCurso').on('submit', function(e) {
           console.log("me envie");
           e.preventDefault();
           var inputs = $("#formCrearCurso :input").serializeArray();
            console.log(inputs);
        
            $.ajax({
            type: "POST",
            url: $("#formCrearCurso").attr("action"),
            data: {
                csrfmiddlewaretoken:inputs[0].value,
                cod_curso: inputs[1].value,
                nom_curso: inputs[2].value
            },
            dataType: "html",
            beforeSend: function(response){   // ANTES QUE SE EJECUTE, O MIENTRAS SE EJECUTA
                // antes de enviar la peticion
                console.log("reealizando...");
            },
            success: function (response) {
                if(response == "correcto"){
                    swal("Correcto!", "El curso se ha registrado con éxito.", "success");
                }
                console.log(response);
            },
            error: function (response) {
                console.log(response)
            }
        });
    
       })
    })
    