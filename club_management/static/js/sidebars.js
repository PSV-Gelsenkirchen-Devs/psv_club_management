/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})();


document.addEventListener("DOMContentLoaded", function(event) {
  var url = window.location.href;
  var element = document.getElementsByClassName('active');
  if(element.length) {
    element[0].classList.add('text-white');
    element[0].classList.remove('active');
  }

  element = document.getElementsByClassName('nav-link');
  for(i=0; i<element.length; i++){
    if(element[i].href == url){
      element[i].classList.add('active');
      element[i].classList.remove('text-white');
    }
  }
});


