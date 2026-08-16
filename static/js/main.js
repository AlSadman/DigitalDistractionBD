/*
=====================================================
MAIN FRONTEND INTERACTION
=====================================================
*/


document.addEventListener(
"DOMContentLoaded",
()=>{


console.log(
"Digital Behaviour System Loaded"
);





const cards =
document.querySelectorAll(
".radio-card"
);





cards.forEach(card=>{


card.addEventListener(
"click",
()=>{


cards.forEach(item=>{


if(
item.querySelector("input").name
===
card.querySelector("input").name
){

item.classList.remove(
"selected"
);

}


});



card.classList.add(
"selected"
);



});


});




});