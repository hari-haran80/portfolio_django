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