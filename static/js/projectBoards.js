$("#input").css("display","none");
$(".editItemTab").css("display","none")
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
});

$(document).on("click",".x",function(){
    $(this).parent().parent().css("display","none")
    $(this).parent().parent().prev().css("display","block")
});

$(document).on("click",".x2",function(){
    $(this).parent().parent().slideUp(200,function(){
        $(this).css("display","none")
        $(this).prev().slideDown(200,function(){
            $(this).css("display","block")
        })
    })
})

$(document).on("click",".editItem",function(){
    $(this).parent().slideUp(200,function(){
        $(this).css("display","none");
        $(this).next().slideDown(200,function(){
            $(this).next().css("display","block")
        });
    });
});

$(document).on("click","backSimpleTaskSlide",function(){
    let text = $(this).parent().parent();
    text.slideUp(200, function(){
        $(this).css("display","none")
        $(this).prev().slideDown(200,function(){
            $(this).css("display","block")
        })
    })
})
