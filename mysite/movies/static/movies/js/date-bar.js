var data = [{"genre": "Horror", "count": 2}, {"genre": "Drama", "count": 11}, {"genre": "Action/Adventure", "count": 22}, {"genre": "Suspense/Thriller", "count": 1}];

var genres = data.map(function(t) {
  return t.genre
})

var margin = {top: 10, right: 5, bottom: 50, left: 50};
// here, we want the full chart to be 700x200, so we determine
// the width and height by subtracting the margins from those values
var fullWidth = 500;
var fullHeight = 200;
// the width and height values will be used in the ranges of our scales
var width = fullWidth - margin.right - margin.left;
var height = fullHeight - margin.top - margin.bottom;
var svg = d3.select('#date-bar-holder').append('svg')
  .attr('width', fullWidth)
  .attr('height', fullHeight)
  .classed('bar-svg', true)
  // this g is where the bar chart will be drawn
  .append('g')
    // translate it to leave room for the left and top margins
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

// y = yScale(datum)
// rectHeight = height - yScale(datum)
// y + rectHeight = yScale(datum) + height - yScale(datum) = height

// use the width and height defined above
var genreScale = d3.scaleBand()
  .domain(genres)
  .range([0, width])
  // allow for some padding between bars
  .paddingInner(0.1);

var countScale = d3.scaleLinear()
  .domain([0, d3.max(data, function(d) { return d.count; })])
  .range([height, 0])


// the width of the bars is determined by the scale
var bandwidth = genreScale.bandwidth();

var barHolder = svg.append('g')
  .classed('bar-holder', true);

// draw the bars
barHolder.selectAll('rect.bar')
    .data(data)
  .enter().append('rect')
    .classed('bar', true)
    .attr('x', function(d, i) {
      // the x value is determined using the
      // month of the datum
      return genreScale(d.genre)
    })
    .attr('width', bandwidth)
    .attr('y', function(d) {
      // the y position is determined by the datum's temp
      // this value is the top edge of the rectangle
      return countScale(d.count);
    })
    .attr('height', function(d) {
      // the bar's height should align it with the base of the chart (y=0)
      return height - countScale(d.count);
    })
    .attr('fill', '#D84646')
    .attr('cursor', 'pointer')
    .on("mouseover", function(d) {
      d3.select(this).attr("fill", "#9F1F1F");
    })
    .on("mouseleave", function(d) {
      d3.select(this).attr("fill", "#D84646");
    })
    .on("click", function(d) {
      console.log(encodeURIComponent(d.genre));
      window.location.href = "http://localhost:8000/movies/movies/" + encodeURIComponent(d.genre);
    });

// create the functions used to represent an axis using our month
// and temp scales
var xAxis = d3.axisBottom(genreScale)
  .tickSizeOuter(0)
  .tickPadding(10);
var yAxis = d3.axisLeft(countScale);

// add the axes to your chart
svg.append('g')
  .classed('x axis', true)
  // a horizontal axis is rendered at y=0, so the axis needs to be translated
  // down to the bottom of the chart
  .attr('transform', 'translate(0,' + height + ')')
  // call the axis function on the selection
  .call(xAxis);

svg.append('g')
  .classed('y axis', true)
  .call(yAxis);

var title = svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("font-family", 'Quicksand')
        .style("text-decoration", "underline")
        .text("Date Night Material")
        .classed('bar-title', true);
