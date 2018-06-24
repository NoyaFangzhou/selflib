# selflib

This repository contains all useful self-made modules for research purpose or just for fun.

## plotlib

This is a module for ploting diagram purporse. Now it supports generating the bar, line and pie chart.

### How to use
To use this library, you should first put it under the same directory as the file you want to do the plot.
```[Python]
import plotlib as pl
```
### API Reference
* <b>Generating the Bar Chart</b>


```[Python]
@para	data			Dataset
@para	loc			Location of the image
@para	grplabel		Label for each group under the x-axis
@para	onavg			Whether generate the average group
@para	text			Whether annotate the value on each bar
@para	color			Color list for each bar
@para	legend			Legend Info
@para	title			Title
@para	xlabel			Xlabel on the x-axis
@para	ylabel			Ylabel on the y-axis

bar_plot(data, loc=None, grplabel=None, onavg=False, text=False, color=None, legend=None, title=None, xlabel=None, ylabel=None)
```


* <b>Generating the Line Chart</b>
```[Python]
@para	data			Dataset
@para	loc			Location of the image
@para	mark			Marker list shown on each point on line
@para	color			Color list for each bar
@para	legend			Legend Info
@para	title			Title
@para	xlabel			Xlabel on the x-axis
@para	ylabel			Ylabel on the y-axis

line_plot(data, loc=None, color=None, mark=None, legend=None, title=None, xlabel=None, ylabel=None)
```

* <b>Generating the Pie Chart</b>
```[Python]
@para	data			Dataset
@para	loc			Location of the image
@para	sangle			The start angle when drawing the pie chart
@para	text			Whether annotate the value on each bar
@para	color			Color list for each bar
@para	legend			Legend Info
@para	title			Title
@para	xlabel			Xlabel on the x-axis
@para	ylabel			Ylabel on the y-axis

pie_plot(data, loc=None, sangle=90.0, text=False, color=None, legend=None, title=None, xlabel=None, ylabel=None)
```
In plotlib directory, we provide a simple example.py file to help you master this module. It can output simple chart for each type.

