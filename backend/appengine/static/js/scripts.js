$(document).ready(function(){
    // clique do checkbox
    var input_fake_checkbox = $("ins.iCheck-helper");
    input_fake_checkbox.click(function(){
        var input_fake = $(this).siblings("input");
        if(typeof input_fake.attr("checked") === typeof undefined){
            input_fake.attr("checked", "checked");
        } else {
            input_fake.removeAttr("checked");
        }
    });
});