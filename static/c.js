$('.apireq').click( function() {
    $.ajax({
             url : "http://127.0.0.1:8000/api/",
             dataType: "json",
             success : function (data) {
                      $('#fname').text( data[0].Firstname);
                      $('#lname').text( data[0].Lastname);
                      $('#street').text(data[0].Street);
                      $('#City').text(data[0].City);
                      $('#Pincode').text(data[0].Pincode);
                      $('#Age').text( data[0].Age);
                    }
                 });
             });