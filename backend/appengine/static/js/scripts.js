$(document).ready(function(){
    // clique do checkbox --- checked active
    var input_fake_checkbox = $("ins.iCheck-helper");
    input_fake_checkbox.click(function(e){
        var input_fake = $(this).siblings("input");
        if(input_fake.attr("checked") === "checked"){
            console.log("sim");
            input_fake.attr("checked", " ");
        } else {
            console.log("nao");
            input_fake.attr("checked", "checked");
        }
    });

    var input_checkbox = $("input.icheck");
    input_checkbox.click(function(e){
        console.log("cicero");
        $(e).hasClass("checked");
    });
});