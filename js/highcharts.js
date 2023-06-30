var chart;

function requestData() {
    $.ajax({
        url: '/live-data',
        success: function (point) {
            var series = chart.series[0],
                shift = series.data.length > 20;
        },
        caches: false
    });
}

$(document).ready(function () {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: "Temperature_data"
        },

        xAxis: {
            type: "Data_time",
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },

        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },

        series: [{
            name: 'temperature',
            data: []
        }]
    });
});