$(document).ready(function() {
    $("form").submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var url = form.attr("action");
        var guess = form.find("input[name='guess']").val();
        $.ajax({
            method: "POST",
            url: url,
            data: {
                guess: guess,
                csrfmiddlewaretoken: form.find("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(data) {
                if (data.result === 'correct') {
                    location.reload();

                } else if(data.result === 'incorrect') {
                    $('#message').css('color', 'red');
                    $('#message').text(data.message);
                    $('#message').addClass("incorrect")
                    $('#message').show();
                    $('.game-img').attr('src', data.image_url);
                    
                    if (data.attempts === 4){
                        $('#guess-form').hide();
                        $('#game-over').show();
                    }
                    
                    
                    

                }
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText);
            }
        });
    });
});
