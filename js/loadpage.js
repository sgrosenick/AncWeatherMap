var page = new WebPage()
var fs = require('fs');

page.onLoadFinished = function() {
    console.log("Page load finished.");
    page.render('export.png');
    fs.write('index.html', page.content, 'w');
    phantom.exit();
};

page.open("https://www.weather.gov/afc/alaskaObs", function() {
    page.evaluate(function(){
    });
});