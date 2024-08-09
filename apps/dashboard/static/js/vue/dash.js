new Vue({
    delimiters: ['[[', ']]'],
    el:'#appDashboard',
    data:{
        anio: 0,
        mes: 0,
        errors: [],
        lists: [],
    },
    created:function(){
        this.listYears();
        this.formVaccine();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2023; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        formVaccine: function(){
            let anio = $("#anio").val();
            let mes = $("#mes").val();
            anio == 0 ? this.anio = new Date().getFullYear() : this.anio = anio;
            mes == 0 ? this.mes = new Date().getMonth() + 1 : this.mes = mes;

            axios.get('api/', { params: { anio: this.anio, mes: this.mes } })
            .then(respuesta => {
                this.lists = respuesta.data;
            });
        },

        PrintExcel: function(){
            url_ = window.location.origin + window.location.pathname + 'print/?anio='+this.anio+'&mes='+this.mes;
            window.open(url_, '_parent');
        }
    }
})