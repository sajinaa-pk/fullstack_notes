$(document).ready(function(){
    $("#Signup").validate({
        rules:{
            fname:{
                required:true,
                minlength:4
            },
            sname:{
                required:true
            },
            email:{
                required:true,
                email:true
            },
            password:{
                required:true,
                maxlength:8,
                minlength:4
            },
            day:{
                required:true,

            },
            month:{
                required:true,
            },
            year:{
                required:true,
            }
        },
        messages:{
            fname:{
                required:"your name here ",
                minlength:"atleast 4"
            }

        }
    });
});