new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPackPregnant',
    data:{
        errors: [],
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        PrintExcel() {
            let tipo = $("#tipo").val();
            let eess = $("#eess").val();
            let anio = $("#anio").val();
            let mes = $("#mes").val();
            url_ = window.location.origin + window.location.pathname + '/printExcel/?tipo='+tipo+'&eess='+eess+'&anio='+anio+'&mes='+mes;
            window.open(url_, '_parent');
        },
    },
})
