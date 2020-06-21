$(document).on("click","#sideNavButton",function(){
    $("#sideNav").css({"width":"250px", "padding-right":"10px","padding-left":"10px"});
})

$(document).on("click","#closeSideNav",function(){
    $("#sideNav").css({"width":"0px", "padding-right":"0px","padding-left":"0px"});
})

$(document).on("click",".dropdownButton",function(){
    $(this).next().slideToggle()
}) 