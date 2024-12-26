
const hamburger = document.querySelector('.hamburger');
const menu_move = document.querySelector('.header__content');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  menu_move.classList.toggle('active_menu');
  
});