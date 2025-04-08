let SlidePosition = 0;       // Intial value for the Position

const Sliders = document.querySelectorAll('.slider-items');
const totalSliders = Sliders.length;



// Previous and Next Buttons Click Event

const Previous = document.getElementById('previous');
const Next = document.getElementById('next');

Previous.addEventListener('click', function() {
    PreviousSlide();
});
Next.addEventListener('click', function() {
    NextSlide();
});

// Update Position Common for all

function UpdatePosition() {
    Sliders.forEach(slide => {
        slide.classList.remove('active');
        slide.classList.add('hidden');
    });

    Sliders[SlidePosition].classList.add('active');

    dots.forEach(dot => {
        dot.classList.remove('activeDot');
    });

    dots[SlidePosition].classList.add('activeDot');
}


// Previous and Next Buttons Functions

function PreviousSlide() {
    if (SlidePosition === 0) {
        SlidePosition = totalSliders - 1;
    } else {
        SlidePosition--;
    }
    UpdatePosition();
}

function NextSlide() {
    if (SlidePosition === totalSliders - 1) {
        SlidePosition = 0;
    } else {
        SlidePosition++;
    }
    UpdatePosition();
}


// Create Dots According to the Number of Images

const dotContainer = document.querySelector('.dots');
Sliders.forEach(slide => {
    const dot = document.createElement('div');
    dot.classList.add('dot');
    dotContainer.appendChild(dot);
});

const dots = document.querySelectorAll('.dot');
dots[SlidePosition].classList.add('activeDot');


// Click Event for Dots

dots.forEach((dot , index)=> {
    dot.addEventListener('click', function(){
        SlidePosition = index;
        UpdatePosition();
    });
});


// Auto Slider script

setInterval(()=>{
    if(SlidePosition == totalSliders -1){
        SlidePosition = 0;
    }
    else{
        SlidePosition++;
    }
    UpdatePosition();
},3000);