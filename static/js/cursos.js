$(document).ready(function () {

    $('#buscar_curso').keyup(function (e) { //el KeyUp es para solicitar una petición Ajax 
                                        //cada vez que el usuario presione una tecla dentro del input
        consulta = $("buscar_curso").val();
        $.ajax({
            type: "GETs",
            url: "/listacursos/",
            data: {'nombre': consulta },
            dataType: "json",
            success: function (data) {
                console.log(data[0].nombre);
            },
            error: function(response) {
                console.log("ME MORI");
            }
        });
    });
});

/*$(document).ready(function () {
    $("#boton").on(function (e) { 
        e.preventDefault();
        input = $("#buscar_curso").val();
        $.ajax({
            type: "GET",
            url: "cursos/",
            data: { nombre : input },
            dataType: "json",
            success: function (response) {
                console.log("lijtoo")
            },
            error: function(response){
                console.log("FFF")
            }
        });
        
    });
});

/*$(document).ready(function () {
    $("#buscar_curso").keyup(function () { 
        _this = this;
        $.each($("#table tbody tr"), function () { 
            if ($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1)
                $(this).hide();
            else
                $(this).show();
        });
    });
});*/