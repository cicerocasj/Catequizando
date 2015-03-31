$(document).ready(function(){
    // clique do checkbox
    var input_fake_checkbox = $("ins.iCheck-helper");
    input_fake_checkbox.click(function(){
        $(this).siblings("input").attr('checked', $(this).parent().hasClass('checked'));
    });
    var input_avatar = $("#input_avatar");
    var fake_avatar = $("#fake_avatar");
    fake_avatar.click(function(){
        input_avatar.click();
    });
    input_avatar.change(function(){
        //var img = new FileReader();
        //img.load(function(e){
        //    fake_avatar.attr("src", e.target.result);
        //});
        fake_avatar.attr("src", input_avatar.val());
        //img.readAsDataURL(input_avatar.file())
    });
});