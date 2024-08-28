new Vue({
    delimiters: ['[[', ']]'],
    el:'#appGoalsPrior',
    data:{
        errors: [],
        list: [],
        totales: [],
        totales2: [],
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2024; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
        },

        listDat: function(){
            let eess = $("#eess").val();
            let anio = $("#anio").val();
            console.log(eess, anio);
            axios.get('list/', { params: { eess: eess, anio: anio } })
            .then(respuesta => {
                this.list = respuesta.data[0];
                this.totales = respuesta.data[1];
                this.totales2 = respuesta.data[2];
                console.log(respuesta.data);
            });
        },

        PrintExcel() {
            let eess = $("#eess").val();
            let anio = $("#anio").val();
            url_ = window.location.origin + window.location.pathname + 'printExcel/?eess='+eess+'&anio='+anio;
            window.open(url_, '_parent');
        },
    },
})
