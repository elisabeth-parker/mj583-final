function initMap() {
  console.log("inside initMap");
  //call my API to get Theaters
  //for loop for each object:
      //create new var with lat and long
      //var pos = {lat: t.lat, lng: t.lng};
      //create new marker and add to maps
      // var marker = new google.maps.Marker({
      //   position: pos,
      //   map: map
      // });

  var mid_US = {lat: 39.500, lng: -98.350};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: mid_US
  });
}

function populateMap() {
  console.log("inside populateMap");
  for (t=0; t<window.movies.data.length; t++) {
    var latitude = window.movies.data[t].lat;
    var longitude = window.movies.data[t].long;
    var theater = window.movies.data[t].name;
    console.log(theater + ": Lat: " + latitude + ", Lng: " + longitude);
    var pos = {lat: parseFloat(latitude), lng: parseFloat(longitude)};
    var marker = new google.maps.Marker({
      position: pos,
      setMap: map
    });
  };
  var sample_lat = window.movies.data[0].lat;
  var sample_lng = window.movies.data[0].long;
  var sample_pos = {lat: parseFloat(sample_lat), lng: parseFloat(sample_lng)};
  var sample_marker = new google.maps.Marker({
    position: sample_pos,
    setMap: map
  });
};
