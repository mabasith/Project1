import csv
from string import Template

timing_data = []
with open('') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

colum_chart_data = [["Test Name", "Diff from Avg"]]

table_data = [["Test Name", "Run Time (s)"]]

for row in timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    try:
        current_run_time = float(row[1])
        avg_run_time = float(row[2])
    except:
        print(row[1])
        print(row[2])
    diff_from_avg = avg_run_time - current_run_time
    colum_chart_data.append([test_name, diff_from_avg])
    table_data.append([test_name,current_run_time])

html_string = Template("""<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
      var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);


  }
</script>

</head>
<body>
<div id="chart_div" style="width:800; height:600"></div>

</body>
</html>""")

chart_data_str =''
for row in colum_chart_data[1:]:
    chart_data_str += '%s,\n'%row
completed_html = html_string.substitute(labels = colum_chart_data[0], data = chart_data_str)  
with open('column_chart.html','w') as f:
    f.write(completed_html)

