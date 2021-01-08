$(document).ready(function () {
    $("#boton").on("click", function () {
        var consulta = $("#buscar_curso").val();    
    
    $('#buscar_curso').keyup(function (e) { //el KeyUp es para solicitar una petición Ajax 
                                        //cada vez que el usuario presione una tecla dentro del input
        e.preventDefault();

        console.log(consulta);
        $.ajax({
            type: "GET",
            url: "/listacursos/",
            data: {nombre: consulta},
            dataType: "json",
            success: function (response) {
                console.log("LO LOGREE")
                console.log(response[0].fields.cod_curso)//data[0].nombre);
                $("#table").DataTable();
            },
            error: function(response) {
                console.log("ME MORI");
            }
        });
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