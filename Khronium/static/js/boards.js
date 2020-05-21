$(".form").css("display","none")
$(".updateBoard").css("display","none")
$(".deleteBoard").css("display","none")

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
});

$(".updateButton").click(function(){
    let boardDetails = $(this).parent().parent();
    boardDetails.slideUp(500, function(){
       boardDetails.css("display","none");
       boardDetails.next().slideDown(500,function(){
        boardDetails.next().css("display","block");
       });
    });
});

$(".closeUpdate").click(function(){
    let updateBoard = $(this).parent().parent();
    updateBoard.slideUp(500,function(){
        updateBoard.css("display","none");
        updateBoard.prev().slideDown(500,function(){
            updateBoard.prev().css("display","block")
        })
    });
});

$(".deleteButton").click(function(){
    let boardDetails = $(this).parent().parent();
    boardDetails.slideUp(500, function(){
       boardDetails.css("display","none");
       boardDetails.next().next().slideDown(500,function(){
        boardDetails.next().next().css("display","block");
       });
    });
});

$(".refuseButton").click(function(){
    let deleteBoard = $(this).parent();
    deleteBoard.slideUp(500,function(){
        deleteBoard.css("display","none");
        deleteBoard.prev().prev().slideDown(500,function(){
            deleteBoard.prev().prev().css("display","block")
        })
    });
});