$(document).ready(function(){
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
        }, function () {
            $(this).toggleClass('big-letter normal-text')
            $(this).text(val)
        })
    })
    // alert($('.circle'))
    // $('.circle').each(function () {
    //     $(this).hover(function () {
    //         console.log('in')
    //     }, function () {
    //         console.log('out')
    //     });
    //     console.log('eachs')
    // }
});

