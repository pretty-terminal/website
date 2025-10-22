document.addEventListener('DOMContentLoaded', function() {
  var navIcon = document.getElementById('nav-icon3');
  var aside = document.querySelector('.div-aside');
  
  navIcon.addEventListener('click', function() {
    navIcon.classList.toggle('open');
    aside.classList.toggle('active'); 
  });
});

const collapsibleItems = document.querySelectorAll(".collapsible");

collapsibleItems.forEach((item) => {
  item.addEventListener("click", () => {
    item.classList.toggle("active");
  });
});

