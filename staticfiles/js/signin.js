//  view password script 

let eyeicon = document.getElementById('eyeicon')
let SecondEyeicon = document.getElementById('eyeicon1')
let password = document.getElementById('password')
let SecondPassword = document.getElementById('password2')

eyeicon.onclick = function(){
    if(password.type == "password"){
        password.type = "text";
        eyeicon.src = "../static/images/eye-open.png";
    }
    else{
        password.type = "password";
        eyeicon.src = "../static/images/eye-close.png";
    }
}

SecondEyeicon.onclick = function(){
    if(SecondPassword.type == "password"){
        SecondPassword.type = "text";
        SecondEyeicon.src = "../static/images/eye-open.png";
    }
    else{
        SecondPassword.type = "password";
        SecondEyeicon.src = "../static/images/eye-close.png";
    }
}