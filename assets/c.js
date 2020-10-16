$('.apireq').click( function() {
    $.ajax({
             url : "http://localhost:8000/studentsapi",
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