/* Display modify button on hover. */
$('.section').ready(function() {
    var section = $('.section');
    section.on('mouseenter', function() {
        $(this).find('.modify_btn').show();
    });
    section.on('mouseleave', function() {
        $(this).find('.modify_btn').hide();
    });
});

$(document).on('click', '.modify_btn', function() {
    /* Display update form. */
    $('#user_profile_update_form').show();
});