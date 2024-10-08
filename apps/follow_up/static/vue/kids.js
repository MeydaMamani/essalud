new Vue({
    delimiters: ['[[', ']]'],
    el:'#appFollow',
    data:{
        dat_pqt: [],
        dat_anemia: [],
        dat_gest: [],
        dat_inmuno: [],
        errors: [],
        viewLinePqt: false,
        viewLineAnemia: false,
        viewLineGest: false,
        viewInmunization: false
    },
    created:function(){

    },
    methods:{
        formSearch:function(){
            const self = this
            const type = $("#type").val();
            const doc = $("#doc").val();
            if(doc == ''){
                new PNotify({
                    title: 'Error!',
                    text: 'Debe ingresar el dni...',
                    type: 'error',
                    styling: 'fontawesome',
                    delay: 3000,
                });
            }else{
                self.viewLineAnemia = false
                self.viewLinePqt = false
                self.viewLineGest = false
                self.viewInmunization = false
                $(".carga").show();
                $(".carga").html('<div class="lds-roller mt-5 text-end"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>');
                axios.get('search/', { params: { type: type, doc: doc  } })
                .then(function (respuesta) {
                    $(".carga").hide();
                    if(respuesta.data == ''){
                        self.viewLineAnemia = false
                        self.viewLinePqt = false
                        self.viewLineGest = false
                        self.viewInmunization = false
                        new PNotify({
                            title: 'Error!',
                            text: 'Usuario No Encontrado...',
                            type: 'notice',
                            styling: 'fontawesome',
                            delay: 3000,
                        });
                    }
                    else{
                        if(type == 1){
                            self.viewLineAnemia = false
                            self.viewLinePqt = true
                            self.viewLineGest = false
                            self.viewInmunization = false
                            self.dat_pqt = respuesta.data[0].fields
                        }
                        else if(type == 2){
                            self.viewLineGest = true
                            self.viewLineAnemia = false
                            self.viewLinePqt = false
                            self.viewInmunization = false
                            self.dat_gest = respuesta.data[0].fields
                        }
                        else if(type == 3){
                            self.viewInmunization = true
                            self.viewLineAnemia = false
                            self.viewLinePqt = false
                            self.viewLineGest = false
                            self.dat_inmuno= respuesta.data
                        }
                        else if(type == 4){
                            self.viewLineAnemia = true
                            self.viewLinePqt = false
                            self.viewLineGest = false
                            self.viewInmunization = false
                            self.dat_anemia = respuesta.data[0].fields
                        }
                    }
                });
            }
        },
    },
})