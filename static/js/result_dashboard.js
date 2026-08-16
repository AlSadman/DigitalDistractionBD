/*
=====================================================
RESULT DASHBOARD CHART
=====================================================
*/


document.addEventListener(
"DOMContentLoaded",
function(){


const chartElement =
document.getElementById(
"resultChart"
);



if(!chartElement)
return;




new Chart(

chartElement,

{

type:"radar",


data:{


labels:[

"Digital Distraction",

"Academic Impact",

"Social Impact",

"Focus"

],



datasets:[{


label:
"Behaviour Profile",


data:[

70,

60,

45,

75

],


borderWidth:3



}]


},




options:{


responsive:true,


maintainAspectRatio:false,


scales:{


r:{


beginAtZero:true,

max:100,

ticks:{


display:false


}


}


}



}



}



);


});
