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

    input_avatar.change( function(event) {
        var tmppath = URL.createObjectURL(event.target.files[0]) || "/static/images/avatars/none.png";
        fake_avatar.fadeIn("fast").attr('src',tmppath);
    });

    //multiple select
    multiple_selects = $('.chosen-select');
    multiple_selects.chosen('.chosen-select');
});

function delete_form(){
    $('#delete_form').submit()
}
