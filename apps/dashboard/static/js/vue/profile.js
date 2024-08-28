const appProfile = new Vue({
    delimiters: ['[[', ']]'],
    el: '#appForPassword',
    data: {
        errors: [],
        lists: [],
    },

    methods: {
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
                    url: '/person/crudUser/',
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
                        $('.change_pw').modal('hide')
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