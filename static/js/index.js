$(document).ready(function(){ //Hacia arriba
    irArriba();
  });
  
  function irArriba(){
    $('.ir-arriba').click(function(){ $('header,html').animate({ scrollTop:'0px' },1000); });
    $(window).scroll(function(){
      if($(this).scrollTop() > 0){ $('.ir-arriba').slideDown(600); }else{ $('.ir-arriba').slideUp(600); }
    });
    $('.ir-abajo').click(function(){ $('header,html').animate({ scrollTop:'1000px' },1000); });
  }