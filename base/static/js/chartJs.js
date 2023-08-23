
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Disaster Report', 'Rate'],
  ['Accidents', 80],
  ['Fire Outbreake', 20],
  ['Weather', 40],
  ['Earth' , 4],
  ['Storm', 8]
]);

  var options =
   {'title':'My Average Day',  'width':550,'height':400,is3D: true};

  var chart =
  new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
