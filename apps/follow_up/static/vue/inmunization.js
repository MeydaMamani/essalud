new Vue({
    delimiters: ['[[', ']]'],
    el:'#appInmunization',
    data:{
        lists: [],
        edad: 1,
        data: false,
    },
    created:function(){

    },
    methods:{
        form: function(){
            let eess = $("#eess").val();
            let edad = $("#edad").val();
            this.data = false
            $(".carga").show();
            $(".carga").html('<div class="lds-roller mt-5 text-end"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>');
            axios.get('list/', { params: { eess: eess, edad: edad } })
            .then(respuesta => {
                $(".carga").hide();
                this.data = true
                this.lists = respuesta.data;
                setTimeout(function() {
                    $('table').trigger('footable_redraw');
                }, 100);
            });
        },

        PrintExcel: function(){
            let eess = $("#eess").val();
            url_ = window.location.origin + window.location.pathname + 'print/?eess='+eess+'&edad='+this.edad;
            window.open(url_, '_parent');
        }
    },
})