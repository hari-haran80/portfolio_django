//  view password script 

let eyeicon = document.getElementById('eyeicon')
let password = document.getElementById('password')

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