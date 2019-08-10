$(document).ready(function() {
     $('#submit').click(function(event) {
       $(document).load('/question #address,#wiki,#map');
       $.ajax({
          data : {
             question : $('#question').val(),
                 },
             type : 'POST',
             url : '/question',
       })
     });
});
