import pygal

def create_graph(file_name, value):
    for key in sorted(value):
        line_chart = pygal.Bar()
        line_chart.x_labels = map(str, range(1945, 2015))
        line_chart.add(key, value[key])
        line_chart.render_to_file('../static/svg/' + file_name + '_' + key + '.svg')

    #create graph mix
    line_chart = pygal.Bar()
    line_chart.x_labels = map(str, range(1945, 2015))
    for key in sorted(value):
        line_chart.add(key, value[key])
    line_chart.render_to_file('../static/svg/' + file_name + '_all.svg')

create_graph()
