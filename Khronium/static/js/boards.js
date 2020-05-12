$(".form").css("display","none")
$("#addBoard").click(function(){
    $("#info").slideUp(500,function(){
        $(this).css("display","none");
        $(".form").slideDown(500,function(){
            $(this).css("display","block")
        })
    });
});

$("#closeAdd").click(function(){
    $(".form").slideUp(500,function(){
        $(this).css("display","none")
        $("#info").slideDown(500,function(){
            $(this).css("display","block")
        })
    })
})