$(function() {
    $('#sendBtn').bind('click', function() {
        msg = $('#msg').val()
        $.getJSON('/send_message', {msg: msg}, function(data) {
            if (data['success'])
                $('#msg').val('')
            })
    });
});

function validate(name) {
   return name.length >= 2;
}