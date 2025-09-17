document.addEventListener('DOMContentLoaded', function () {
  const navIcon = document.getElementById('nav-icon3');
  const asideDiv = document.getElementById('aside-div');

  navIcon.addEventListener('click', function () {
    navIcon.classList.toggle('open');
    asideDiv.classList.toggle('aside-div-show');
  });
});
