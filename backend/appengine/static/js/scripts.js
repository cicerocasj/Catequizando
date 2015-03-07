$(document).ready(function(){
    // clique do checkbox --- checked active
    var input_fake_checkbox = $("ins.iCheck-helper");
    input_fake_checkbox.click(function(e){
        console.log("cicero");

        //$(e).hasClass("checked");
    });

    var input_checkbox = $("input.icheck");
    input_checkbox.click(function(e){
        console.log("cicero");
        $(e).hasClass("checked");
    });
});