new Vue({
    delimiters: ['[[', ']]'],
    el:'#appCoverage',
    data:{
        errors: [],
        list: [],
        listDistricts: [],
    },
    created:function(){
        this.listYears();
        this.formVaccine();
    },
    methods:{
        listYears: function(){
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));
        },

        formVaccine: function(){
            let eess = $("#eess").val();
            let mes = $("#mes").val();
            mes == 0 ? this.mes = new Date().getMonth() + 1 : this.mes = mes;
            var nameMonth = new Date(this.mes.toString()).toLocaleString('default', { month: 'long' });
            $('#nameMonthMenor1Anio').text(nameMonth.toUpperCase()+' '+new Date().getFullYear());

            axios.get('list/', { params: { eess: eess, month: this.mes } })
            .then(respuesta => {
                this.list = respuesta.data[0];
            });
        },

        PrintExcelRn: function(){
            let eess = $("#eess").val();
            url_ = window.location.origin + window.location.pathname + 'printNominal/?eess='+eess+'&mes='+this.mes;
            window.open(url_, '_parent');
        }
    }
})