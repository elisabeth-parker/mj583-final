// Global container for movie data
window.movies = {
    params: {},
    data: {},
};

// fetchData
function fetchData() {
    // $.get("/api/?" + $.param(window.movies.params))
    $.get("http://localhost:8000/movies/api/theaters/")
        .done(function(data) {
            $('#raw-json').text(JSON.stringify(data, null, '  '));
            window.movies.data=data.Data;
            console.log(window.movies.data);
            populateMap();
        })
        .fail(function(){
            console.log("Could not load data");
            alert("Could not load data");
        });

    console.log("about to return data");


}


// init wires up watchers on selections and fetches new data
function init(){
  fetchData();
    // var countrySel = $('#sel-country');
    // var categorySel = $('#sel-category');
    // var genderSel = $('#sel-gender');
    //
    // function updateSelections() {
    //     var params = window.movies.params || {};
    //     params.country = countrySel.val();
    //     params.category = categorySel.val();
    //     params.gender = genderSel.val();
    //     fetchData();
    // }
    //
    // countrySel.on('change', updateSelections);
    // categorySel.on('change', updateSelections);
    // genderSel.on('change', updateSelections);
    // updateSelections();

    // Initalize map
    //initMap(window.movies);
  }

// Call init on DOMReady
$(init);
