document.getElementById('signupForm').addEventListener('submit', function(event) {
    var password = document.getElementById('password').value;
    var errorMessage = '';

    if (password.length < 8) {
        errorMessage = 'Password must be at least 8 characters long.';
    }

    if (errorMessage) {
        event.preventDefault();
        document.getElementById('passwordError').textContent = errorMessage;

        setTimeout(function() {
            passwordError.textContent = '';
        }, 5000);
    }
});


// Validating First Name
document.addEventListener('DOMContentLoaded', function() {
    const firstNameInput = document.getElementById('First_name');
    const FnameValidation = document.querySelector('.FNameValidation');

    function validateName() {
        const lettersOnlyRegex = /^[A-Za-z]+$/;

        FnameValidation.innerHTML = '';

        let isValid = true;

        if (!lettersOnlyRegex.test(firstNameInput.value)) {
            FnameValidation.innerHTML += 'Please enter letters only.';
            isValid = false;
        }

        if (isValid) {
            FnameValidation.style.display = 'none';
        } 
        else {
            FnameValidation.style.display = 'block';
        }
    }

    firstNameInput.addEventListener('input', validateName);
});
    

//  Validating Last Name  

document.addEventListener('DOMContentLoaded', function(){
    const lastNameInput = document.getElementById('Last_name');
    const LnameValidation = document.querySelector('.LNameValidation');
    function validateLName() {
        const lettersOnlyRegex = /^[A-Za-z]+$/;
        LnameValidation.innerHTML = '';
        let isValid = true;
        if (!lettersOnlyRegex.test(lastNameInput.value)) {
            LnameValidation.innerHTML += 'Please enter letters only.';
            isValid = false;
        }
        if (isValid) {
            LnameValidation.style.display = 'none';
        } 
        else {
            LnameValidation.style.display = 'block';
        }
    }
    lastNameInput.addEventListener('input', validateLName);
});