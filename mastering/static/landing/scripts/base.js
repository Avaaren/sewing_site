
$(function(){
  $(window).scroll(function(){
    if (window.scrollY > 250) {
      $('.sidebar').show(200);
    }
    else{
      $('.sidebar').hide(200);
    }
  });

  $('.navbar_ul_item').hover(
    function(){
      $(this).find('ul.navbar_sub_ul').show(200);

    },  
    function(){
      $(this).find('ul.navbar_sub_ul').hide(300);
    } 
  );

  $('.navbar_sub_ul_item').hover(
    function(){
      $(this).find('ul.navbar_second_level_sub_ul').show(200);
      
    },  
    function(){
      $(this).find('ul.navbar_second_level_sub_ul').hide(300);
    } 
  );  
  
});