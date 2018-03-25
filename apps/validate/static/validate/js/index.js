
$(document).ready(function(){
    $("#register").hide();
    $("#login").hide();

    $("#select").on("click", "button", function(){
        if($(this).text() === 'Register')
        {
            $("#register").show();
            $("#login").hide();
            $("button:nth-of-type(2)").hide();
            $("button:nth-of-type(1)").show();
        }
        else if($(this).text() === 'Login') {
            $("#login").show();
            $("#register").hide();
            $("button:nth-of-type(1)").hide();
            $("button:nth-of-type(2)").show();
        }
    });

    if ($('span').text() === '1'){
        $("#register").show();
        $("#login").hide();
        $("button:nth-of-type(2)").hide();
        $("button:nth-of-type(1)").show();
    }
    else if($('span').text() === '2'){
        $("#login").show();
        $("#register").hide();
        $("button:nth-of-type(1)").hide();
        $("button:nth-of-type(2)").show();
    }

});
