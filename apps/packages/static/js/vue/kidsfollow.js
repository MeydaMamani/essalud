new Vue({
    delimiters: ['[[', ']]'],
    el:'#appKidsFollow',
    data:{
        lists: [],
        errors: [],
        total: 0,
        cumple: 0,
        nocumple: 0,
        avan: 0,
        anio: 0,
        mes: 0,
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

        sendFormat: function (e) {
            var self = this
            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)

            if(this.anio == 0){
                this.anio = new Date().getFullYear();
                formData.set('anio', this.anio);
            }
            if(this.mes == 0){
                this.mes = 1;
                formData.set('mes', this.mes);
            }

            var nameMonth = new Date(this.mes.toString()).toLocaleString('default', { month: 'long' });
            $('.nameMonthYear').text(nameMonth.toUpperCase()+' '+this.anio);

            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'boys/api/',
                data: formData
            }).then(response => {
                self.lists = response.data
                self.total = response.data[0].total
                self.cumple = response.data[0].cumple
                self.nocumple = response.data[0].total - response.data[0].cumple
                self.avan = response.data[0].avance

                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                    $('.chart').data('easyPieChart').update(self.avan);
                    $('.chart').data('easyPieChart').options.barColor = '#8899cc';
                }, 100);
            }).catch(e => {
                this.errors.push(e)
            })
        },

        PrintExcel() {
            let eess = $("#eess").val();
            url_ = window.location.origin + window.location.pathname + '/printExcel/?eess='+eess+'&anio='+this.anio+'&mes='+this.mes;
            window.open(url_, '_parent');
        },
    },
})