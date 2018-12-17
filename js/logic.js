$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "http://localhost:7001/all"
    }).done(function(data){
        var header= document.createElement("h1");
        header.innerText = ("News Headlines");
        $("#newsFeed").append(header);
        $("#newsFeed").append($('<ul id="news_list"/>'));
        var parsedNews= JSON.parse(data);
        parsedNews.forEach(function (element){
            var link= document.createElement("a");
            link.href = element['link'];
            link.innerText = element['title'];
            $("#newsFeed ul").append($("<li/>").html(link));
        });
    });
})