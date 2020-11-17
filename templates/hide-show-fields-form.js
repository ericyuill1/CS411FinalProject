$("#crudChoices").change(function() {
    if ($(this).val() == "search" || $(this).val() == "insert" || $(this).val() == "delete") {
        $('#baseDiv').show();
        $('#baseDiv').attr('required', '');
        $('#baseDiv').attr('data-error', 'This field is required');

        $('#updateDiv').hide();
        $('#updateDiv').removeAttr('required');
        $('#updateDiv').removeAttr('data-error');
    } else {
        $('#updateDiv').show();
        $('#updateDiv').attr('required', '');
        $('#updateDiv').attr('data-error', 'This field is required');

        $('#baseDiv').hide();
        $('#baseDiv').removeAttr('required');
        $('#baseDiv').removeAttr('data-error');
    }
});
$("#crudChoices").trigger("change");