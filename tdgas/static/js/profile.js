/* Display modify button on hover. */
$('.section').ready(function() {
    var section = $('.section');
    section.on('mouseenter', function() {
        if (!$(section).find('.modify_btn').hasClass('disabled'))
            $(this).find('.modify_btn').show();
    });
    section.on('mouseleave', function() {
        $(this).find('.modify_btn').hide();
    });
});

/* Display update form on click. */
$(document).on('click', '.modify_btn', function() {
    var userProfileUpdateForm   = $('#user_profile_update_form');
    var modifyBtn               = $(userProfileUpdateForm.parents('.section')).find('.modify_btn');
    userProfileUpdateForm.show();
    modifyBtn.addClass('disabled');
    modifyBtn.hide();
    $('.update_btn_container').show();
});

/* Restore original UI on cancel. */
$(document).on('click', '.user_update_cancel_btn', function() {
    var userProfileUpdateForm   = $('#user_profile_update_form');
    var modifyBtn               = $(userProfileUpdateForm.parents('.section')).find('.modify_btn');
    userProfileUpdateForm.hide();
    $('.update_btn_container').hide();
    modifyBtn.removeClass('disabled');
    modifyBtn.show();
});

/* AJAX call to update user profile. */
function updateUserProfile(firstname, lastname, addr_street, addr_suburb, addr_state, addr_postal) {
    $.ajax({
        type: 'POST',
        url : '/profile_update/',
        data: {
            'first_name'       :   firstname   ,
            'last_name'        :   lastname    ,
            'address_street'   :   addr_street ,
            'address_suburb'   :   addr_suburb ,
            'address_state'    :   addr_state  ,
            'address_postcode' :   addr_postal
        },
        statusCode: {
            201: function() {
                /* On succeed: */
                alert('Updating succeeded!');
            },
            406: function() {
                /* On fail: */
                alert('Updating failed!');
            }
        },
        success: function() {}
    });
}

/* Update user info on submit. */
$(document).on('click', '.user_update_btn', function() {
    var firstname   = $('#firstname_input'  ).val();
    var lastname    = $('#lastname_input'   ).val();
    var addr_street = $('#addr_street_input').val();
    var addr_suburb = $('#addr_suburb_input').val();
    var addr_state  = $('#addr_state_input' ).val();
    var addr_postal = $('#addr_postal_input').val();
    updateUserProfile(firstname, lastname, addr_street, addr_suburb, addr_state, addr_postal);
});