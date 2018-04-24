var map;

function initMap() {
  var mid_NC = {lat: 35.900, lng: -78.873};
  map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: mid_NC
    });
}

function populateMap() {
  //for each theater in the data from fetchData, which is stored in global container
  for (t=0; t<window.movies.data.length; t++) {
    var theater = window.movies.data[t];
    var id = theater.th_id;
    var latitude = theater.lat;
    var longitude = theater.long;
    var address = theater.address;
    var city = theater.city;
    var county;
    console.log(movies);

    //info for infoWindow
    var name = theater.name;
    var infoWindow = new google.maps.InfoWindow({
      maxWidth: 300
    });

    //create a new map marker and add it to the map
    var pos = {lat: parseFloat(latitude), lng: parseFloat(longitude)};

    //bin theaters by county
    if (city == "Durham") {
      county = "Durham County";
      //create marker
      var marker = new google.maps.Marker({
        position: pos,
        icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
        content: '<div id="content">'+
            '<a href="/movies/theaters/' + id + '" target="_blank"><h1 id="firstHeading" class="firstHeading">' + name + '</h1></a>' + '<div><p>' + address + '</p></div>' +
            '</div>',
        map: map
      });

    } else if (city == "Chapel Hill") {
      county = "Orange County";
      var marker = new google.maps.Marker({
        position: pos,
        icon: 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png',
        content: '<div id="content">'+
            '<a href="/movies/theaters/' + id + '" target="_blank"><h1 id="firstHeading" class="firstHeading">' + name + '</h1></a>' + '<div><p>' + address + '</p></div>' +
            '</div>',
        map: map
      });

    } else {
      county = "Wake County";
      var marker = new google.maps.Marker({
        position: pos,
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
        content: '<div id="content">'+
            '<a href="/movies/theaters/' + id + '" target="_blank"><h1 id="firstHeading" class="firstHeading">' + name + '</h1></a>' + '<div><p>' + address + '</p></div>' +
            '</div>',
        map: map
      });
    }

    //make window pop up on click
    //thanks to StackOverflow user H.M. for this code suggestion
    marker.addListener('mouseover', function() {
      infoWindow.setContent(this.content);
      infoWindow.open(this.getMap(), this);
    });

  };
};
