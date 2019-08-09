$(document).ready(function() {
     $('form').on('load', function(event) {
       $.ajax({
          data : {
             question : $('#question').val(),
                 },
             type : 'POST',
             url : '/question',
       })
     });
});
