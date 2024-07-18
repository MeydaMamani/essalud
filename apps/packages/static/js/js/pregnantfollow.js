
$("#btnSend").click(function(){
    var anio = $("#anio").val();
    var mes = $("#mes").val();

    if (anio != 0 && mes != 0){
        document.getElementById("btnSend").type = "submit";
    }
    else if(anio == 0){
        new PNotify({
            title: 'Error!',
            text: 'Seleccione un Año',
            type: 'error',
            styling: 'fontawesome',
            delay: 2000,
        });
    }else if(mes == 0){
        new PNotify({
            title: 'Error!',
            text: 'Seleccione un Mes',
            type: 'error',
            styling: 'fontawesome',
            delay: 2000,
        });
    }
});