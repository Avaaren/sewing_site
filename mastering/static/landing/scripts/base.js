let el = document.querySelectorAll('.navbar_ul_item, .navbar_sub_ul_item');
    for (let i = 0; i < el.length; i++) {
      el[i].addEventListener('mouseenter', showMenu, false);
      el[i].addEventListener('mouseleave', hideMenu, false);
    }
    function showMenu() {
      if (this.children.length > 1) {
        this.children[1].style.height = 'auto';
        this.children[1].style.opacity = '1';
        this.children[1].style.overflow = 'visible';
      }
      else {
        return false
      }
    }
    function hideMenu() {
      if (this.children.length > 1) {
        this.children[1].style.height = '0';
        this.children[1].style.opacity = '0';
        this.children[1].style.overflow = 'hidden';
      }
      else {
        return false
      }
    }