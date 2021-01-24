
$("#addPrograma").submit(function(){
    var codigo = $('input[name="codigo"]').val().trim();
    var nombre = $('input[name="nombre"]').val().trim();
    var contenido = $('input[name="contenido"]').val().trim();

    if(codigo && nombre && contenido){
        $.ajax({
            url: '{% url "crearprograma" %}',
            data: {
                'cod_programa': codigo,
                'nom_programa': nombre,
                'contenido_Aca': contenido
            },
            dataType: 'json',
            success: function (data) {
                if (data.programa) {
                  appendToUsrTable(data.programa);
                }
            }
        });
    }else{
        alert("All fields must have a valid value.");
    }
    $('#addPrograma').trigger("reset");
    return false;
});

function appendToUsrTable(programa) {
    $("#ProgramTable > tbody:last-child").append(`
          <tr id="programa-${programa.cod_programa}">
              <td class"codigoprograma programdata">${programa.cod_programa}</td>
              '<td class"nombreprograma programdata">${programa.nom_programa}</td>
              '<td class"contenidoaca programdata">${programa.contenido_Aca}</td>
              '<td align="center">
                  <button class="btn btn-success form-control" onClick="editProgram(${programa.cod_programa})" data-toggle="modal" data-target="#myModal")">EDIT</button>
              </td>
              <td align="center">
                  <button class="btn btn-danger form-control" onClick="deleteProgram(${programa.cod_programa})">DELETE</button>
              </td>
          </tr>
      `);
  }

  $("#updatePrograma").submit(function() {
    var codigo = $('input[name="formCodigo"]').val().trim();
    var nombre = $('input[name="formNombre"]').val().trim();
    var contenido = $('input[name="formContenido"]').val().trim();
    
    if (codigo && nombre && contenido) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "actualizarprograma" %}',
            data: {
                'cod_programa': codigo,
                'nom_programa': nombre,
                'contenido_Aca': contenido
                
            },
            dataType: 'json',
            success: function (data) {
                if (data.programa) {
                  updateToProgramTable(data.programa);
                }
            }
        });
       } else {
        alert("All fields must have a valid value.");
    }
    $('#updatePrograma').trigger("reset");
    $('#myModal').modal('hide');
    return false;
});

// Update Django Ajax Call
function editProgram(cod_programa) {
  if (cod_programa) {
    tr_cod = "#programa-" + cod_programa;
    codigo = $(tr_cod).find(".codigoprograma").text();
    nombre = $(tr_cod).find(".nombreprograma").text();
    contenido = $(tr_cod).find(".contenidoaca").text();
    
    $('#form-codigo').val(codigo);
    $('#form-nombre').val(nombre);
    $('#form-contenido').val(contenido);
  }
}
function updateToProgramTable(programa){
    $("#ProgramTable #programa-" + programa.cod_programa).children(".programdata").each(function() {
        var attr = $(this).attr("name");
        if (attr == "codigo") {
          $(this).text(programa.cod_programa);
        } else if (attr == "nombre") {
          $(this).text(programa.nom_programa);
        } else {
          $(this).text(programa.contenido_Aca);
        }
      });
}

  