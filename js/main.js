$(function() {
    "use strict";

    // Maintenance mode check:
    if (window.siteMaintenance && window.siteMaintenance.enabled) {
        if (!window.location.pathname.toLowerCase().includes('underconstruction.html')) {
            window.location.replace('underconstruction.html');
            return;
        }
    }

	
	/* ==========================================================================
   Flex menu
   ========================================================================== */
	$(".flexy-menu").flexymenu({speed: 400, indicator: true});
	


   /* ==========================================================================
   Preload
   ========================================================================== */
    
    $(window).load(function() {
        
        $("#status").fadeOut();
        
        $("#preloader").delay(1000).fadeOut("slow");
    });

	
	/* ==========================================================================
     Textrotator
     ========================================================================== */   

    $(".rotate").textrotator({
        animation: "dissolve",
        separator: ",",
        speed: 2500
    });



    /* ==========================================================================
     For anchor smooth scroll
     ========================================================================== */  
    $('a[href*=#]').on('click', function(event){     
        event.preventDefault();
        $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
    });
      	
	



});






