new Vue({
    delimiters: ['[[', ']]'],
    el:'#appFollow',
    data:{
        dat_person: [],
        errors: [],
        consol_users: false,
    },
    created:function(){

    },
    methods:{
        formSearch:function(){
            const self = this
            const type = $("#type").val();
            const doc = $("#doc").val();
            axios.get('search/', { params: { type: type, doc: doc  } })
            .then(function (respuesta) {
                self.consol_users = true
                self.dat_person = respuesta.data[0].fields;
                console.log(self.dat_person);
                // self.form_detail.name_member = respuesta.data.fields.full_name;
                // self.form_detail.member = respuesta.data.fields.pk;
                // setTimeout(() => $('.show-tick').selectpicker('refresh'));
            });
        },
    },
})