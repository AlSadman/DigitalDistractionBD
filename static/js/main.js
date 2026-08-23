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


    // Sidebar Toggle Logic
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const mobileCloseBtn = document.getElementById("mobileCloseBtn");
    const sidebar = document.getElementById("sidebar");
    const sidebarOverlay = document.getElementById("sidebarOverlay");
    const body = document.body;

    function toggleSidebar(show) {
        if (show) {
            sidebar.classList.add("active");
            sidebarOverlay.classList.add("active");
            body.style.overflow = "hidden";
        } else {
            sidebar.classList.remove("active");
            sidebarOverlay.classList.remove("active");
            body.style.overflow = "";
        }
    }

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", () => toggleSidebar(true));
    }
    if (mobileCloseBtn) {
        mobileCloseBtn.addEventListener("click", () => toggleSidebar(false));
    }
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener("click", () => toggleSidebar(false));
    }


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