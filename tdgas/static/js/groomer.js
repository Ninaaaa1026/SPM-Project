
/* Display details on click. */
$(document).on('click', '.appointment_details_btn', function() {
    var appointmentDetails   = $('#appointment_details');
    var detailsBtn           = $(appointmentDetails.parents('.section')).find('.appointment_details_btn');
    /*var user                =$('#appointment_user')
    getdetails(user)*/
    appointmentDetails.show();
    detailsBtn.addClass('disabled');
    detailsBtn.hide();
    $('.hide_btn').show();
});

/* Restore original UI on cancel. */
$(document).on('click', '.hide_btn', function() {
    var appointmentDetails   = $('#appointment_details');
    var hideBtn               = $(appointmentDetails.parents('.section')).find('.hide_btn');
    appointmentDetails.hide();
    $('.hide_btn').hide();
    $('.appointment_details_btn').show();
});

function getdetails(subscriber){
    $.ajax({
        type = 'GET',
        url = '/groom_details/',
        data = {'user' : subscriber}

    })
}