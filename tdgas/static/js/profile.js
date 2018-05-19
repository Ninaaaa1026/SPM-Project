/* AJAX functions.
 * ***********************************************************************************************/
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
                console.log('Profile updating succeeded!');
                $('#user_firstname_header').text(firstname  );
                $('#addr_street'          ).text(addr_street);
                $('#addr_suburb'          ).text(addr_suburb);
                $('#addr_state'           ).text(addr_state );
                $('#addr_postcode'        ).text(addr_postal);
            },
            406: function() {
                /* On fail: */
                console.log('Profile updating failed!'   );
            }
        },
        success: function() {}
    });
}

/* AJAX call to update user contact. */
function updateUserContact(contactType, phoneNumber) {
    $.ajax({
        type: 'POST',
        url : '/contact_update/',
        data: {
            'contact_type' : contactType,
            'phone_number' : phoneNumber
        },
        statusCode: {
            201: function() {
                /* On succeed: */
                console.log(contactType + ' updating succeeded!');
                if (contactType == 'mobile')
                    $('#contact_mobile').text(phoneNumber);
                else if (contactType == 'home')
                    $('#contact_home'  ).text(phoneNumber);
                else
                    $('#contact_work'  ).text(phoneNumber);
            },
            406: function() {
                /* On fail: */
                console.log(contactType + ' updating failed!'   );
            }
        },
        success: function() {}
    });
}

/* AJAX call to update dog information. */
function updateDogInfo(dogId, dogName, dogBreed, dogDoB) {
    $.ajax({
        type: 'POST',
        url : '/dog_update/',
        data: {
            'id'        : dogId     ,
            'dog_name'  : dogName   ,
            'dog_breed' : dogBreed  ,
            'dog_dob'   : dogDoB
        },
        success: function(data) {
            $('#dogs_container').html($(data).find('#dogs_container'));
        }
    });
}

/* Display modify button on hover.
 * ***********************************************************************************************/
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

/* Update user profile.
 * ***********************************************************************************************/
/* Display user update form on click. */
$(document).on('click', '#user_profile_modify_btn', function() {
    var modifyBtn               = $(this);
    var parentSection           = modifyBtn.parents('.section');
    var userProfileUpdateForm   = parentSection.find('#user_profile_update_form');
    modifyBtn.addClass('disabled');
    modifyBtn.hide();
    parentSection.find('.update_btn_container').show();
    userProfileUpdateForm.show();
});

/* Restore original user UI on cancel. */
$(document).on('click', '#user_update_cancel_btn', function() {
    var cancelBtn               = $(this);
    var parentSection           = cancelBtn.parents('.section');
    var userProfileUpdateForm   = parentSection.find('#user_profile_update_form');
    var modifyBtn               = parentSection.find('.modify_btn');
    modifyBtn.removeClass('disabled');
    modifyBtn.show();
    parentSection.find('.update_btn_container').hide();
    userProfileUpdateForm.hide();
});

/* Update user info on submit. */
$(document).on('click', '#user_update_btn', function() {
    var updateBtn = $(this);
    var parentSection = updateBtn.parents('.section');
    /* Update profile info. */
    var firstname   = parentSection.find('#firstname_input'     ).val();
    var lastname    = parentSection.find('#lastname_input'      ).val();
    var addr_street = parentSection.find('#addr_street_input'   ).val();
    var addr_suburb = parentSection.find('#addr_suburb_input'   ).val();
    var addr_state  = parentSection.find('#addr_state_input'    ).val();
    var addr_postal = parentSection.find('#addr_postal_input'   ).val();
    updateUserProfile(firstname, lastname, addr_street, addr_suburb, addr_state, addr_postal);

    /* Update contact info. */
    var mobile      = parentSection.find('#contact_mobile_input').val();
    var home        = parentSection.find('#contact_home_input'  ).val();
    var work        = parentSection.find('#contact_work_input'  ).val();
    updateUserContact('mobile', mobile);
    updateUserContact('home'  , home  );
    updateUserContact('work'  , work  );

    /* Hide update form after updating. */
    parentSection.find('#user_update_cancel_btn').click();
});

/* Update dog info.
 * ***********************************************************************************************/
/* Display dog update form on click. */
$(document).on('click', '.dog_modify_btn', function() {
    var modifyBtn               = $(this);
    var parentSection           = modifyBtn.parents('.section');
    modifyBtn.addClass('disabled');
    modifyBtn.hide();
    parentSection.find('.update_btn_container').show       (              );
    parentSection.find('.dog_name_input'      ).removeAttr ('readonly'    );
    parentSection.find('.dog_name_input'      ).removeClass('input_trans' );
    parentSection.find('.dog_name_input'      ).addClass   ('update_input');
    parentSection.find('.dog_breed_display'   ).hide       (              );
    parentSection.find('.dog_breed_input'     ).show       (              );
    parentSection.find('.dog_dob_display'     ).hide       (              );
    parentSection.find('.dog_dob_input'       ).show       (              );
});

/* Restore original dog UI on cancel. */
$(document).on('click', '.dog_update_cancel_btn', function() {
    var cancelBtn               = $(this);
    var parentSection           = cancelBtn    .parents('.section');
    var modifyBtn               = parentSection.find('.modify_btn');
    modifyBtn.removeClass('disabled');
    modifyBtn.show();
    parentSection.find('.update_btn_container').hide       (              );
    parentSection.find('.dog_name_input'      ).attr       ('readonly'    );
    parentSection.find('.dog_name_input'      ).addClass   ('input_trans' );
    parentSection.find('.dog_name_input'      ).removeClass('update_input');
    parentSection.find('.dog_breed_display'   ).show       (              );
    parentSection.find('.dog_breed_input'     ).hide       (              );
    parentSection.find('.dog_dob_display'     ).show       (              );
    parentSection.find('.dog_dob_input'       ).hide       (              );
});

/* Update dog info on submit. */
$(document).on('click', '.dog_update_btn', function() {
    var updateBtn       = $(this);
    var parentSection   = updateBtn    .parents('.section');
    var dogId           = parentSection.find('.dog_id'         ).val();
    var dogName         = parentSection.find('.dog_name_input' ).val();
    var dogBreed        = parentSection.find('.dog_breed_input').val();
    var dogDoB          = parentSection.find('.dog_dob_input'  ).val();
    /* Update dog info. */
    updateDogInfo(dogId, dogName, dogBreed, dogDoB);
    /* Hide update form after updating. */
    parentSection.find('.user_update_cancel_btn').click();
});

/* Switch dog and appointment display.
 * ***********************************************************************************************/
$(document).on('click', '#switch_btn', function() {
    var switchBtn = $(this);
    if (switchBtn.hasClass('show_dogs')) {
        switchBtn.removeClass('show_dogs'        );
        switchBtn.addClass   ('show_appointments');
        switchBtn.text       ('Show your dogs >' );
        $('#dogs_container')        .hide();
        $('#appointments_container').show();
    }
    else {
        switchBtn.removeClass('show_appointments'        );
        switchBtn.addClass   ('show_dogs'                );
        switchBtn.text       ('Show your appointments >' );
        $('#appointments_container').hide();
        $('#dogs_container')        .show();
    }
});

/* Display and hide add form on click.
 * ***********************************************************************************************/
// Show add form on click.
$(document).on('click', '.btn_add', function() {
    var addBtn  = $(this);
    var addForm = $(this).parent().find('.section');
    addBtn .hide();
    addForm.show();
});

// Restore add button on cancel.
$(document).on('click', '.add_update_cancel_btn', function() {
    var addForm = $(this).parents('.add_section').find('.section');
    var addBtn  = $(this).parents('.add_section').find('.btn_add');
    addForm.hide();
    addBtn .show()
});