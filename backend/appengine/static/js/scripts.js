$(document).ready(function(){
    // clique do checkbox
    var input_fake_checkbox = $("ins.iCheck-helper");
    input_fake_checkbox.click(function(){
        $(this).siblings("input").attr('checked', $(this).parent().hasClass('checked'));
    });
});