function submitToAPI(e) {
       e.preventDefault();
       var URL = "https://abc1234.execute-api.us-east-1.amazonaws.com/01/contact";

       var email = $("#email-input").val();
       var pass = $("#password-input").val();
       var number = $("#number-input").val();
       var data = {
          email : email,
          pass : pass,
          number : number
        };

       $.ajax({
         type: "POST",
         url : "https://abc1234.execute-api.us-east-1.amazonaws.com/01/contact",
         dataType: "json",
         crossDomain: "true",
         contentType: "application/json; charset=utf-8",
         data: JSON.stringify(data),


         success: function () {
           // clear form and show a success message
           alert("Successfull");
           document.getElementById("contact-form").reset();
       location.reload();
         },
         error: function () {
           // show an error message
           alert("UnSuccessfull");
         }});
     }
