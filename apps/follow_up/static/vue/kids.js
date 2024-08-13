new Vue({
    delimiters: ['[[', ']]'],
    el:'#appFollow',
    data:{
        dat_pqt: [],
        dat_anemia: [],
        dat_gest: [],
        errors: [],
        viewLinePqt: false,
        viewLineAnemia: false,
        viewLineGest: false
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
                axios.get('search/', { params: { type: type, doc: doc  } })
                .then(function (respuesta) {
                    if(respuesta.data == ''){
                        self.viewLineAnemia = false
                        self.viewLinePqt = false
                        self.viewLineGest = false
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
                            self.dat_pqt = respuesta.data[0].fields
                        }
                        else if(type == 2){
                            self.viewLineGest = true
                            self.viewLineAnemia = false
                            self.viewLinePqt = false
                            self.dat_gest = respuesta.data[0].fields
                        }
                        else if(type == 4){
                            self.viewLineAnemia = true
                            self.viewLinePqt = false
                            self.viewLineGest = false
                            self.dat_anemia = respuesta.data[0].fields
                        }
                    }
                });
            }
        },
    },
})