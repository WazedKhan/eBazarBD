$document.on('click', '#add-to-cart', function(e){
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "{%url ''%}",
        data: "data",
        dataType: "dataType",
        success: function (response) {

        }
    });
})