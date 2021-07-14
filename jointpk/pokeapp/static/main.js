    //search bar function
    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#post li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        
        });
        
    });