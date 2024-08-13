//  Toggle Button for Navigation 

const button = document.getElementById('menu-icon');
const nav = document.querySelector('.head_nav');
const blackScreen = document.querySelector('.BlackScreen');

button.addEventListener('click', () => {
    if(button.classList.contains('fa-bars')){
        button.classList.remove('fa-bars');
        button.classList.add('fa-times');
        nav.style.left = '0px'
        blackScreen.style.left = '0px'
    }else{
        button.classList.remove('fa-times');
        button.classList.add('fa-bars');
        nav.style.left = '-60%'
        blackScreen.style.left = '-100%'
    }
});

blackScreen.addEventListener('click', () => {
    if(button.classList.contains('fa-bars')){
        button.classList.remove('fa-bars');
        button.classList.add('fa-times');
        nav.style.left = '0px'
        blackScreen.style.left = '0px'
    }else{
        button.classList.remove('fa-times');
        button.classList.add('fa-bars');
        nav.style.left = '-60%'
        blackScreen.style.left = '-100%'
    }
})

// Nav Color change when scrolling

window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navigation');
    const drowpdown = document.querySelector('.projects');
    
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        drowpdown.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    } else {
        navbar.style.backgroundColor = 'transparent';
        drowpdown.style.backgroundColor = 'transparent';
    }
});

// Managing Active Status for Navigation Bar

const activePage = window.location.pathname;
const navLink = document.querySelectorAll('.link').forEach(link =>{
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active');
    }
});

// changing button status script when submitting

function DeleteReviewBtn (){
    const DeleteReviewBtn = document.getElementById('DeleteReviewBtn');
    DeleteReviewBtn.textContent = 'Deleting...';
    DeleteReviewBtn.disabled = true;
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


// rating form submition 

function validateForm() {
            
    var ratings = document.getElementsByName('rating');
    var ratingSelected = false;
    
    for (var i = 0; i < ratings.length; i++) {
        if (ratings[i].checked) {
            ratingSelected = true;
            break;
        }
    }

    if (!ratingSelected) {
        
        var errorMessage = document.querySelector('.RatingErrorMessage');
        errorMessage.innerHTML = '*Please select a rating';
        
        // Message disappear Script

        setTimeout(function (){
            errorMessage.style.display = 'none';
        }, 2000);
        
        return false;
    }

    // Button changing Script when submiting

    const WriteReviewBtn = document.getElementById('WriteReviewBtn');
    WriteReviewBtn.disabled = true;
    WriteReviewBtn.textContent = 'Posting...';

    return true;
}
