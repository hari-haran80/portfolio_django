var toggled = false;
function toggle(){
    if(!toggled){
        toggled = true;
        document.querySelector('.head_nav').style.left = "0px";
        return;
    }
    if(toggled){
        toggled = false;
        document.querySelector(".head_nav").style.left = "-60%";
        return;
    }
}
// Write Review
var mainDiv = document.querySelector('.form_main_div')
function reviewWrite(){
    mainDiv.style.display = 'block';
}

var close = document.querySelector('.fa-xmark')
function CloseReview(){
    mainDiv.style.display = 'none';
}

// Iframe showing script

function showFrame(id) {
    var iframeContainer = document.getElementById('iframeContainer');
    var iframe = document.getElementById('overlayIframe');
    iframe.src = "/update/" + id+"/";           
    iframeContainer.style.display = 'block'

    while (iframeContainer.firstChild) {
        iframeContainer.removeChild(iframeContainer.firstChild);
    }

    iframeContainer.appendChild(iframe);
}