new Vue({
    delimiters: ['[[', ']]'],
    el:'#appPerson',
    data:{
        edit: false,
        addperson: false,
        listperson: false,
        existuser: false,
        form: {},
        formPass: {},
        doc: '',
        pid: '',
    },
    methods:{
        searchPerson(){
            var self = this
            axios.get('searchperson/', { params: { dni: this.doc } })
            .then(function (response) {
                if (response.data.length > 0) {
                    console.log(response.data);
                    self.listperson = true
                    self.addperson = false
                    self.person = response.data[0].fields
                    self.person.pk = response.data[0].pk
                    if (response.data.length == 1) {
                        self.existuser = false
                    }
                    else{
                        self.existuser = true
                        self.pid = response.data[1].pk
                    }
                }
                else{
                    self.addperson = true
                    self.listperson = false
                    self.edit = false
                    self.form = {}
                    self.form.pdoc = self.doc
                    new PNotify({
                        title: 'Usuario No Encontrado!',
                        text: 'Crear usuario...',
                        type: 'error',
                        styling: 'fontawesome',
                        delay: 2000,
                    });
                }
            });
        },

        editPerson(e){
            this.form = e
            this.edit = true
            this.addperson = true
            this.listperson = false
        },

        sendPerson: function (e) {
            this.edit ? this.personUpdate(e) : this.personCreate(e);
        },

        personCreate:function (e) {
            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)
            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'POST',
                url: 'cperson/',
                data: formData
            }).then(response => {
                if(response.data =='success'){
                    new PNotify({
                        title: 'No se guardo el registro!',
                        text: 'El usuario ya Existe o complete campos obligatorios',
                        type: 'error',
                        styling: 'fontawesome',
                        delay: 3000,
                    });
                }
                else{
                    this.person = response.data[0].fields
                    this.person.pk = response.data[0].pk
                    this.listperson = true
                    this.addperson = false
                    this.existuser = false
                    new PNotify({
                        title: 'Registro Exitoso!',
                        text: 'Datos guardados correctamente...',
                        type: 'success',
                        styling: 'fontawesome',
                        delay: 3000,
                    });
                }
            }).catch(e => {
                this.errors.push(e)
            })
        },

        personUpdate:function (e) {
            var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
            var formData = new FormData(e.target)
            axios({
                headers: { 'X-CSRFToken': csrfmiddlewaretoken, 'Content-Type': 'multipart/form-data' },
                method: 'PUT',
                url: 'cperson/',
                data: formData
            }).then(response => {
                if(response.data =='success'){
                    new PNotify({
                        title: 'No se guardo el registro!',
                        text: 'Ingrese campos obligatorios',
                        type: 'error',
                        styling: 'fontawesome',
                        delay: 3000,
                    });
                }
                else{
                    this.person = response.data[0].fields
                    this.listperson = true
                    this.addperson = false
                    this.edit = false
                    new PNotify({
                        title: 'Registro Actualizado!',
                        text: 'Datos modificados correctamente...',
                        type: 'success',
                        styling: 'fontawesome',
                        delay: 3000,
                    });
                }
            }).catch(e => {
                this.errors.push(e)
            })
        },

        sendPass:function(e) {
            const password = $("#password").val();
            const password_r = $("#password_r").val();
            var self = this
            if ((password && password_r) && (password == password_r)){
                var csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
                var bodyFormData = new FormData(e.target);
                axios({
                    headers: { 'X-CSRFToken': csrfmiddlewaretoken,'Content-Type': 'multipart/form-data' },
                    method: 'PUT',
                    url: 'crudUser/',
                    data: bodyFormData
                }).then(response => {
                    if(response.status=='200'){
                        new PNotify({
                            title: 'Éxito!',
                            text: 'Se cambio la contraseña correctamente...',
                            type: 'success',
                            styling: 'fontawesome',
                            delay: 2000,
                        });
                        self.formPass = {}
                    }
                }).catch(e => {
                    this.errors.push(e)
                })
            }
            else{
                new PNotify({
                    title: 'Error!',
                    text: 'No coinciden las contraseñas...',
                    type: 'error',
                    styling: 'fontawesome',
                    delay: 2000,
                });
            }
        },
    },
})