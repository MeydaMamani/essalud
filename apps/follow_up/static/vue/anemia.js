new Vue({
    delimiters: ['[[', ']]'],
    el:'#appAnemia',
    data:{
        errors: [],
        list: [],
        listDistricts: [],
        listEess: [],
        listNomAnemia: [],
        listTotProv: [],
        listeessDx: [],
        mes: 0,
        anio: 0,
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

        formAnemia: function(e) {
            var self = this
            self.anio == 0 ? self.anio = new Date().getFullYear() : self.anio = self.anio;
            self.mes == 0 ? self.mes = new Date().getMonth() + 1 : self.mes = self.mes;
            var nameMonth = new Date(self.mes.toString()).toLocaleString('default', { month: 'long' });
            $('#nameMonth').text(nameMonth.toUpperCase()+' '+self.anio);

            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)
            formData.set('anio', self.anio);
            formData.set('mes', self.mes);

            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'searchAnemia/',
                data: formData
            }).then(response => {
                self.listTotProv = response.data[0];
                self.listNomAnemia = response.data[1];
                self.listeessDx = response.data[2];

            }).catch(e => {
                this.errors.push(e)
            })
        },

        PrintExcelRn: function(){
            let eess = $("#eess").val();
            let tipo = $("#tipo").val();
            url_ = window.location.origin + window.location.pathname + 'printNominal/?&eess='+eess+'&tipo='+tipo+'&anio='+this.anio+'&mes='+this.mes;
            window.open(url_, '_parent');
        }
    }
})