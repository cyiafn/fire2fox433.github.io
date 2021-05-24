function submitFormTextCount(){

    var formData = {
        text: $("#textInput").val().toString()
      };
    formData = JSON.stringify(formData);
    console.log(formData);
    
    $.ajax({
        url: 'https://k9zb7anlsh.execute-api.us-east-1.amazonaws.com/prod/textCount',
        type: 'POST',
        crossDomain: true,
        dataType: 'json',
        data: formData.toString(),
        encode: true,
        success: function(data) {
            if (data["status_code"] == 200){
                $('#textCountFail').hide();
                $('#textCountSuccess').html("Characters: " + data["data"]["chars"] + "      Words: "+data["data"]["words"]);
                $('#textCountSuccess').show();
            }
            else{
                $('#textCountSuccess').hide();
                $('#textCountFail').show();
            }
            
        },
        error: function(data){
            $('#textCountFail').show();
            $('#textCountSuccess').hide();
            console.log("FAILED: %s",data)
        }
    });
}