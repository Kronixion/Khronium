$("#input").css("display","none");

$("#addList").click(function(){
    $("#addButton").slideUp(200,function(){
        $("#addButton").css("display","none");
        $("#input").slideDown(200,function(){
            $("#input").css("display","block");
        })
    });
});

$("#X").click(function(){
    $("#input").slideUp(200,function(){
        $(this).css("display","none");
        $("#addButton").slideDown(200,function(){
            $(this).css("display","block")
        });
    });
});

$(".itemInput").css("display","none")

$(document).on("click",".AddItems",function(){
    $(this).css("display","none");
    $(this).next().css("display","block");
})

$(document).on("click",".x",function(){
    $(this).parent().parent().css("display","none")
    $(this).parent().parent().prev().css("display","block")
})