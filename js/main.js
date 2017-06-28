//function to initialize the leaflet map
function createMap() {
    //creates the map
    var myMap = L.map('map', {
        center: [61.162, -149.9],
        zoom: 11.5
    });
    
    //Add OSM basemap
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>',
        maxZoom: 22
    }).addTo(myMap);
    
    //call getData function
    //getData(myMap);
};

//Import GEOJSON data
function getData(map) {
    //load the data
    $.ajax("data/oldagedependancy.geojson", {
        dataType: "json",
        success: function(response) {
            //create an attributes array
            var attributes = processData(response);
            
            //call function to create proportional symbols
            createPropSymbols(response, map, attributes);
            //create slider
            createSequenceControls(map, attributes);
            //create legend
            createLegend(map, attributes);
        }
    });
};

$(document).ready(createMap);