const Cursordot = document.querySelector('.cursor-dot');
const outline = document.querySelector('.cursor-outline');

window.addEventListener("mousemove", function (e){
    const posX = e.clientX;
    const posY = e.clientY;

    Cursordot.style.left = `${posX}px`;
    Cursordot.style.top = `${posY}px`;

    outline.animate({
        left : `${posX}px`,
        top : `${posY}px`
    },{duration:500, fill : "forwards"});
});

document.addEventListener('mousedown', ()=> Cursordot.classList.add('active'))
document.addEventListener('mouseup', ()=> Cursordot.classList.remove('active'))
