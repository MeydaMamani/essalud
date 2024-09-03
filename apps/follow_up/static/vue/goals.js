new Vue({
    delimiters: ['[[', ']]'],
    el:'#appGoalsPrior',
    data:{
        errors: [],
        nameCa: [],
        totGeneral: [],
        avGeneral: [],
        totalAct: [],
        totalActDetail: [],
        totalAvActDetail: [],
        subactividades: [],
        actividad: [],
        advanceAct: []
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
            axios.get('list/', { params: { eess: eess, anio: anio } })
            .then(respuesta => {
                this.nameCa = respuesta.data[0];
                this.totGeneral = respuesta.data[1];
                this.avGeneral = respuesta.data[2];
                this.totalAct = respuesta.data[3];
                this.totalActDetail = respuesta.data[4];
                this.totalAvActDetail = respuesta.data[5];
                this.subactividades = respuesta.data[6];
                this.actividad = respuesta.data[7];
            });
        },

        btnAdvActividad: function(){
            let eess = $("#eess").val();
            let anio = $("#anio").val();
            let act = $("#actividad").val();
            axios.get('avance/', { params: { eess: eess, anio: anio, act: act } })
            .then(respuesta => {
                this.advanceAct = respuesta.data
                $('#chartAdvance').remove();
                $('.chartnino').append("<canvas id='chartAdvance'></canvas>");
                var ctx = document.getElementById("chartAdvance");
                var chartAdvance = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ["Ene", "feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"],
                        datasets: [{
                            label: "Meta",
                            borderColor: "#03586A",
                            data: [ this.advanceAct.meta, this.advanceAct.meta, this.advanceAct.meta,
                                    this.advanceAct.meta, this.advanceAct.meta, this.advanceAct.meta,
                                    this.advanceAct.meta, this.advanceAct.meta, this.advanceAct.meta,
                                    this.advanceAct.meta, this.advanceAct.meta, this.advanceAct.meta ]
                        },
                        {
                            label: "Avance",
                            borderColor: "#26B99A",
                            data: [ this.advanceAct.avAct_ene, this.advanceAct.avAct_feb, this.advanceAct.avAct_mar,
                                    this.advanceAct.avAct_abr, this.advanceAct.avAct_may, this.advanceAct.avAct_jun,
                                    this.advanceAct.avAct_jul, this.advanceAct.avAct_ago, this.advanceAct.avAct_set,
                                    this.advanceAct.avAct_oct, this.advanceAct.avAct_nov, this.advanceAct.avAct_dic ]
                        }]
                    },
                });
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
