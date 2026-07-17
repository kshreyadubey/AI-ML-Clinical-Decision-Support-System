/*=========================================
        AROGYAAI WELCOME
=========================================*/

document.addEventListener("DOMContentLoaded",()=>{

const orbit=document.querySelector(".orbit-system");

if(!orbit) return;

let angle=0;

function animate(){

    angle+=0.08;

    orbit.style.transform=
    `translate(-50%,-50%) rotate(${angle}deg)`;

    requestAnimationFrame(animate);

}

animate();

});