
/* Display details on click. */
$(document).on('click', '.appointment_details_btn', function() {
    var apptID                =$(this).val(); 
    var appointmentDetails   = $('#appointment_details_'+apptID);
    var detailsBtn           = $(appointmentDetails.parents('.section')).find('.appointment_details_btn');

    getdetails(apptID)
    appointmentDetails.show();
    //detailsBtn.addClass('disabled');
    detailsBtn.hide();
    $('.hide_btn').show();
});

/* Restore original UI on cancel. */
$(document).on('click', '.hide_btn', function() {
    var apptID                =$(this).val(); 
    var appointmentDetails   = $('#appointment_details_'+apptID);
    var hideBtn               = $(appointmentDetails.parents('.section')).find('.hide_btn');
    appointmentDetails.hide();
    hideBtn.hide();
    $('.appointment_details_btn').show();
});

function getdetails(apptID){
    $.ajax({
        type : 'GET',
        url : '/groom_details/',
        data : {'appointmentID' : apptID},
        success: function() {}
    });
}
