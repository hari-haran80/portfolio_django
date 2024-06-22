// message disapper script

var messageDiv = document.getElementById('myMessage');
    
function hideMessage() {
    messageDiv.style.opacity = 0;
    setTimeout(function () {
        messageDiv.style.display = 'none';
    }, 500);
}

setTimeout(hideMessage, 3000);