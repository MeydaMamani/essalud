new Vue({
    delimiters: ['[[', ']]'],
    el:'#appGoalsPrior',
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
        },

        PrintExcel() {
            let eess = $("#eess").val();
            let anio = $("#anio").val();
            url_ = window.location.origin + window.location.pathname + 'printExcel/?eess='+eess+'&anio='+anio;
            console.log(url_);
            window.open(url_, '_parent');
        },
    },
})
