function roundToTwo(num) {
return +(Math.round(num + "e+2")  + "e-2");
}

var width = 1160,
height = 500,
radius = Math.min(width, height) / 2;
var legendRectSize = 18;
var legendSpacing = 4;

var tooltip = d3.select("body").append("div").attr("class", "toolTip");

var color = d3.scaleOrdinal(d3["schemeCategory10"])


var arc = d3.arc()
.outerRadius(radius - 10)
.innerRadius(0);

var labelArc = d3.arc()
.outerRadius(radius - 40)
.innerRadius(radius - 40);

var pie = d3.pie()
.sort(null)
.value(function(d) { return d["#repositories"]; });

var svg = d3.select("#pie")
.attr("width", width)
.attr("height", height)
.append("g")
.attr("transform", "translate(" + width  / 2 + "," + height / 2 + ")");



function render(data){
  var sum =0;
  for (var i = 0; i < data.length; i++) {
    sum += data[i]["#repositories"];
  }
  for (var i = 0; i < data.length; i++) {
    data[i]["#repositories"] = roundToTwo(data[i]["#repositories"]/sum *100);
  }

  var g = svg.selectAll(".arc")
    .data(pie(data))
  .enter().append("g")
    .attr("class", "arc");

    g.append("path")
    .attr("d", arc)
    .style("fill", function(d) { return color(d.value); });

    g.append("text")
    .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
    .attr("dy", ".35em")
    .text(function(d) {return d.data["#repositories"]; });

    var legend = svg.selectAll('.legend')
          .data(color.domain())
          .enter()
          .append('g')
          .attr('class', 'legend')
          .attr('transform', function(d, i) {
            var height = legendRectSize + legendSpacing;
            var offset =  height * color.domain().length / 2;
            var horz = -2 * legendRectSize * -10 ;
            var vert = i * height - offset;
            return 'translate(' + horz + ',' + vert + ')';
          });

        legend.append('rect')
          .attr('width', legendRectSize)
          .attr('height', legendRectSize)
          .style('fill', color)
          .style('stroke', color);

        legend.append('text')
          .attr('x', legendRectSize + legendSpacing)
          .attr('y', legendRectSize - legendSpacing)
          .text(function(d,i) { console.log(i);return data[i].name });

}
d3.json("http://localhost:8080\\data\\piechart.json", render);
