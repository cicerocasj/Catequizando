$(document).ready(function(){
    // clique do checkbox --- checked active
    var input_checkbox = $("div.icheckbox_flat-aero");
    input_checkbox.click(function(e){
        $(e).hasClass("checked")
    });
});
