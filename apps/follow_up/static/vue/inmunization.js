new Vue({
    delimiters: ['[[', ']]'],
    el:'#appInmunization',
    data:{
        lists: [],
        lists_cant: [],
        edad: 0,
        anio: 0,
        mes: 0,
        // data: false,
        listRn: false,
        list1anio: false,
        list23anio: false,
        list4anio: false,
        listAdoles: false,
        listGest: false,
        listAdult: false
    },
    created:function(){
        this.listYears();
    },
    methods:{
        listYears: function(){
            let fec = new Date();
            var selectYear = document.getElementById("anio");
            for(var i = 2024; i<=fec.getFullYear(); i++)selectYear.options.add(new Option(i,i));
            var selectMonth = document.getElementById("mes");
            for(var i = 1; i<=12; i++)selectMonth.options.add(new Option(new Date(i.toString()).toLocaleString('default', { month: 'long' }).toUpperCase(),i));

            if(this.anio == 0){
                this.anio = new Date().getFullYear();
            }
            if(this.mes == 0){
                this.mes = new Date().getMonth()+1;
            }
        },

        form: function(){
            let eess = $("#eess").val();
            let edad = $("#edad").val();
            let tipo = $("#tipo").val();
            $(".carga").show();
            $(".carga").html('<div class="lds-roller mt-5 text-end"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>');
            axios.get('list/', { params: { eess: eess, edad: edad, tipo: tipo } })
            .then(respuesta => {
                $(".carga").hide();
                this.lists = respuesta.data;
                if(edad == 0){
                    this.listRn = true
                    this.list1anio = false
                    this.list23anio = false
                    this.list4anio = false
                    this.listAdoles = false
                    this.listGest = false
                    this.listAdult = false
                }
                else if(edad == 1){
                    this.listRn = false
                    this.list1anio = true
                    this.list23anio = false
                    this.list4anio = false
                    this.listAdoles = false
                    this.listGest = false
                    this.listAdult = false
                }
                else if(edad == 2){
                    this.listRn = false
                    this.list1anio = false
                    this.list23anio = true
                    this.list4anio = false
                    this.listAdoles = false
                    this.listGest = false
                    this.listAdult = false
                }
                else if(edad == 4){
                    this.listRn = false
                    this.list1anio = false
                    this.list23anio = false
                    this.list4anio = true
                    this.listGest = false
                    this.listAdult = false
                }
                else if(edad == 5){
                    this.listRn = false
                    this.list1anio = false
                    this.list23anio = false
                    this.list4anio = false
                    this.listAdoles = true
                    this.listGest = false
                    this.listAdult = false
                }
                else if(edad == 6){
                    this.listRn = false
                    this.list1anio = false
                    this.list23anio = false
                    this.list4anio = false
                    this.listAdoles = false
                    this.listGest = true
                    this.listAdult = false
                }
                else if(edad == 7){
                    this.listRn = false
                    this.list1anio = false
                    this.list23anio = false
                    this.list4anio = false
                    this.listAdoles = false
                    this.listGest = false
                    this.listAdult = true
                }

                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                }, 100);
            });
        },

        PrintExcel: function(){
            let eess = $("#eess").val();
            url_ = window.location.origin + window.location.pathname + 'print/?eess='+eess+'&edad='+this.edad;
            window.open(url_, '_parent');
        },

        contInmuni: function(){
            let eess = $("#eess").val();

            axios.get('listCant/', { params: { eess: eess, anio: this.anio, mes: this.mes } })
            .then(respuesta => {
                this.lists_cant = respuesta.data;
                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                }, 100);
            });
        }
    },
})