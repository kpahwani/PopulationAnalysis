var genderData = {}
var relationData = {}
function relationChart () {
	var obj = {}
	var temp = {}
	var data = []
	for(var i = 0; i<relationData.length; i++)
	{
		temp = relationData[i];
		obj = new Object();
		obj.label = temp.relation__value;
		obj.y = temp.count;
		data.push(obj)
	}
	var chart = new CanvasJS.Chart("genderGraphContainer", {
		title:{
			text: "Data Relation Analysis"
		},
		data: [
		{
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "column",
			dataPoints: data
		}
		]
	});
	chart.render();
}

function genderChart() {
	var obj = {}
	var temp = {}
	var data = []
	for(var i = 0; i<genderData.length; i++)
	{
		temp = genderData[i];
		obj = new Object();
		obj.indexLabel = temp.gender;
		obj.y = temp.count;
		data.push(obj)
	}
	var chart = new CanvasJS.Chart("relationGraphContainer",
	{
		title:{
			text: "Data Gender Analysis"
		},
		legend: {
			maxWidth: 350,
			itemWidth: 120
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			legendText: "{indexLabel}",
			dataPoints: data
		}
		]
	});
	chart.render();
}

function getGenderData() {
	$.ajax({
	  dataType: "json",
	  url: "http://127.0.0.1:8000/user/gender_count/",
	  success: function (data) {
		  genderData = data;
		  genderChart(genderData);
      }
	});
}

function getRelationData() {
	$.ajax({
	  dataType: "json",
	  url: "http://127.0.0.1:8000/user/relationship_count/",
	  success: function (data) {
		  relationData = data;
		  relationChart(relationData);
      }
	});
}

function loadCharts() {
	getGenderData();
	getRelationData();
}

function redirect() {
	location.href = "../display/";
}