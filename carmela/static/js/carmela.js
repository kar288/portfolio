$(document).ready(function(){
    var size = 2*$('.big-letter').width()/3
    console.log(size)
    $('.big-letter').css({'fontSize': size})
    $('.inside').each(function() {
        var val = $(this).text().trim()
        $(this).hover(function(){
            if (val == 'M') {
                $(this).text("Open Math Map")
            }
            if (val == 'R') {
                $(this).text("Resume")
            }
            if (val == 'G') {
                $(this).text("Grumblr")
            }
            $(this).toggleClass('normal-text big-letter')
            $('.normal-text').css({'fontSize': size/10})
        }, function () {
            $(this).toggleClass('big-letter normal-text')
            $(this).text(val)
            $('.big-letter').css({'fontSize': size})
        })
    })
});


