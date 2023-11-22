$(function() {
    $('#sendBtn').bind('click', function() {
        msg = $('#msg').val()
        $.getJSON('/run', {msg: msg}, function(data) {
            console.log(data)
        })
        return false;
    });
});

function validate(name) {
   return name.length >= 2;
}