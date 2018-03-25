
$(document).ready(function(){

    $('.rating').each(function(){
        var stars = $(this).html();
        for(var star = 0; star < stars; star++){
            $(this).append('<img src="http://res.freestockphotos.biz/pictures/15/15160-illustration-of-a-gold-star-pv.png">');
        }
    });
});
