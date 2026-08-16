/*
=====================================================
Result Dashboard Chart
Digital Behaviour Analysis System
=====================================================
*/


document.addEventListener(
"DOMContentLoaded",
function(){


const canvas =
document.getElementById(
"behaviourChart"
);



if(!canvas)
return;



const data =
JSON.parse(
canvas.dataset.values
);



new Chart(

canvas,

{

type:"radar",


data:{


labels:[

"Distraction",

"Academic Impact",

"Social Impact",

"Focus"

],



datasets:[{


label:
"Behaviour Profile",


data:data,


fill:true,


borderWidth:3



}]


},



options:{


responsive:true,


scales:{


r:{


beginAtZero:true,


max:100


}


}



}


}



);



});