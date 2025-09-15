from bokeh.plotting import figure
from bokeh.io import curdoc

p = figure(title='Bokeh demo')
p.line([1, 2, 3, 4], [3, 7, 8, 5])

curdoc().add_root(p)
