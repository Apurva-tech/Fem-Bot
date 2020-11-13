/*Only display Retweets*/
window.twttr = (function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0],
        t = window.twttr || {};
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "https://platform.twitter.com/widgets.js";
    fjs.parentNode.insertBefore(js, fjs);

    t._e = [];
    t.ready = function (f) {
        t._e.push(f);
    };

    return t;
}(document, "script", "twitter-wjs"));

twttr.ready(function (twttr) {
    twttr.events.bind("rendered", function (event) {
        var widgetFrame = event.target;
        var retweets = widgetFrame.contentDocument.querySelectorAll("div.timeline-Tweet:not(.timeline-Tweet--isRetweet)");
        console.log(retweets)
        retweets.forEach(function (node) {
            if (node.parentNode) { // (in)sanity check
                node.parentNode.style = 'display: none;' // hide entire parent li tag
            }
        })
    });

});

/*switching sections*/
let navLinks=$('.nav-link')
let sections=$('section')
let anchors=$('.nav-link>a')
let circles=$('.circle')

function clickNav(){
    width = document.body.clientWidth;
    

        let anchor=this.children[0];
        let show=$(anchor).attr('href');
        console.log(show)

        /*Hide all sections*/
        $.each(sections, function(k,v){
            $(v).addClass('hide');
        })

        /*Only show clicked section*/
        $(show).removeClass('hide');


        /*Remove active class from all anchors*/
        $.each(anchors, function(k,v){
            $(v).removeClass('active')
        })

        /*Give active class to current link*/ 
        $(anchor).addClass('active')
        if(width<=768)
        $('nav>ul').css('display', 'none')


        /*remove all circle active classes*/
        $.each(circles, function(k,v){
            $(v).removeClass('circle-active')
            
        })
      
        /*give circle active to current class*/
        let current=show.slice(1,)
        console.log(current)
        $(`.circle-${current}`).addClass('circle-active')
 


}


console.log(sections)
$.each(navLinks, function(key, value){
    $(value).click(clickNav)

})




$.each(circles, function(k,v){

    $(v).click(function(){
        let str=(v.classList[1].slice(7,))
        $(`.${str}-link`).click()
    })

})


$('.menu-icon').click(function(){
    $('nav>ul').toggle('hide')
})

var onresize = function() {
    width = document.body.clientWidth;
    if(width<=768){
        $('nav>ul').css('display', 'none')
    }
    else{
        $('nav>ul').css('display', 'block')
    }
    
}
 window.addEventListener("resize", onresize);
 $( document ).ready(onresize);


 $(document).ready(function() {
    $('#loader').addClass("hide");
 });

