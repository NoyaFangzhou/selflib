#!usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


# draw the bar chart
# @para	data 		Dataset
# @para loc 		Location of the image
# @para grplabel	Label for each group under the x-axis
# @para onavg		Whether generate the average group
# @para text 		Whether annotate the value on each bar
# @para color 		Color list for each bar
# @para legend 		Legend Info
# @para title 		Title
# @para xlabel 		Xlabel on the x-axis
# @para ylabel 		Ylabel on the y-axis
def bar_plot(data, loc=None, grplabel=None, onavg=False, text=False, color=None, legend=None, title=None, xlabel=None, ylabel=None):
	
	# calculate the avg for each datalist and add it to the end
	if onavg:
		for i in xrange(len(data)):
			data[i].append(np.mean(data[i]))
		if grplabel is not None:
			grplabel.append("Average")

	if grplabel is not None:
		assert len(data[0]) == len(grplabel), "Data size doens't match the group number.\nExpected {}, Actual {}".format(len(data[0]), len(grplabel))
	if color is not None:
		assert len(data) <= len(color), "Data size doens't match the given color size.\nExpected {}, Actual {}".format(len(data), len(color))
	if legend is not None:
		assert len(data) <= len(legend), "Data size doens't match the given legend size.\nExpected {}, Actual {}".format(len(data), len(legend))

	# data to plot
	n_groups = len(data[0])

	# create plot
	if loc is None:
		fig, ax = plt.subplots()
	else:
		fig, ax = plt.subplots(figsize=tuple(loc))
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8

	for i in xrange(len(data)):
		if color is None:
			if legend is None:
				rects = plt.bar(index+(bar_width*i), data[i], bar_width, 
					alpha=opacity)
			else:
				rects = plt.bar(index+(bar_width*i), data[i], bar_width, 
					alpha=opacity, 
					label=legend[i])
		else:
			if legend is None:
				rects = plt.bar(index+(bar_width*i), data[i], bar_width, 
					alpha=opacity, 
					color=color[i])
			else:
				rects = plt.bar(index+(bar_width*i), data[i], bar_width, 
					alpha=opacity, 
					color=color[i], 
					label=legend[i])
		if text:
			for rect in ax.patches:
				height = rect.get_height()
				ax.text(rect.get_x() + rect.get_width()/2., 1.025*height, '%.2f' % float(height),
					color='black', 
					fontweight='bold',
		            ha='center', 
		            va='bottom')


	# set the title of img
	if title is not None:
		ax.set_title(title)
	# set the X-Y label of img
	if xlabel is not None:
		ax.set_xlabel(xlabel)
	if ylabel is not None:
		ax.set_ylabel(ylabel)

	plt.xticks(index + bar_width, tuple(grplabel))
	
	if legend is not None:
		plt.legend(loc="best")

	plt.tight_layout()
	plt.show()


# draw the line chart
# @para	data 		Dataset
# @para loc 		Location of the image
# @para mark 		Marker list shown on each point on line
# @para color 		Color list for each bar
# @para legend 		Legend Info
# @para title 		Title
# @para xlabel 		Xlabel on the x-axis
# @para ylabel 		Ylabel on the y-axis

# ================    ===============================
# character           description
# ================    ===============================
#    -                solid line style
#    --               dashed line style
#    -.               dash-dot line style
#    :                dotted line style
#    .                point marker
#    ,                pixel marker
#    o                circle marker
#    v                triangle_down marker
#    ^                triangle_up marker
#    <                triangle_left marker
#    >                triangle_right marker
#    1                tri_down marker
#    2                tri_up marker
#    3                tri_left marker
#    4                tri_right marker
#    s                square marker
#    p                pentagon marker
#    *                star marker
#    h                hexagon1 marker
#    H                hexagon2 marker
#    +                plus marker
#    x                x marker
#    D                diamond marker
#    d                thin_diamond marker
#    |                vline marker
#    _                hline marker
# ================    ===============================
def line_plot(data, loc=None, color=None, mark=None, legend=None, title=None, xlabel=None, ylabel=None):
	if color is not None:
		assert len(data) <= len(color), "Data size doens't match the given color size.\nExpected {}, Actual {}".format(len(data), len(color))
	if legend is not None:
		assert len(data) <= len(legend), "Data size doens't match the given legend size.\nExpected {}, Actual {}".format(len(data), len(legend))
	if mark is not None:
		assert len(data) <= len(mark), "Data sie doesn't match the given marker size. \nExpected {}, Actual {}".format(len(data), len(mark))
	if loc is None:
		fig, ax = plt.subplots()
	else:
		fig, ax = plt.subplots(figsize=tuple(loc))
	
	index = np.arange(len(data[0]))

	for i in xrange(len(data)):
		if color is None:
			if legend is None:
				ax.plot(range(0, len(data[i])), data[i],
					marker=mark[i] if mark is not None else None)
			else:
				ax.plot(range(0, len(data[i])), data[i],
					label=legend[i],
					marker=mark[i] if mark is not None else None)
		else:
			if legend is None:
				ax.plot(range(0, len(data[i])), data[i],
					color=color[i],
					marker=mark[i] if mark is not None else None)
			else:
				ax.plot(range(0, len(data[i])), data[i],
					color=color[i],
					label=legend[i],
					marker=mark[i] if mark is not None else None)

	# set the title of img
	if title is not None:
		ax.set_title(title)
	# set the X-Y label of img
	if xlabel is not None:
		ax.set_xlabel(xlabel)
	if ylabel is not None:
		ax.set_ylabel(ylabel)

	if legend is not None:
		plt.legend(loc="best")
	plt.tight_layout()
	plt.show()


# draw the pie chart
# @para	data 		Dataset
# @para loc 		Location of the image
# @para sangle 		The start angle when drawing the pie chart
# @para text 		Whether annotate the value on each bar
# @para color 		Color list for each bar
# @para legend 		Legend Info
# @para title 		Title
# @para xlabel 		Xlabel on the x-axis
# @para ylabel 		Ylabel on the y-axis
def pie_plot(data, loc=None, sangle=90.0, text=False, color=None, legend=None, title=None, xlabel=None, ylabel=None):
	if color is not None:
		assert len(data) <= len(color), "Data size doens't match the given color size.\nExpected {}, Actual {}".format(len(data), len(color))
	if legend is not None:
		assert len(data) <= len(legend), "Data size doens't match the given legend size.\nExpected {}, Actual {}".format(len(data), len(legend))
	assert sangle <= 360.0 and sangle>=0.0, "Start angle should in range [0.0, 360.0]. \nYours {}".format(sangle)

	if loc is None:
		fig, ax = plt.subplots()
	else:
		fig, ax = plt.subplots(figsize=tuple(loc))

	if color is None:
		if text:
			patches = plt.pie(data, 
				autopct='%1.2f%%',
				shadow=False, 
				startangle=sangle,
				labels=legend if legend is not None else None)
		else:
			patches= plt.pie(data, 
				shadow=False, 
				startangle=sangle,
				labels=legend if legend is not None else None)
	else:
		if text:
			patches = plt.pie(data, 
				autopct='%1.2f%%',
				colors=color, 
				shadow=False, 
				startangle=sangle,
				labels=legend if legend is not None else None)
		else:
			patches= plt.pie(data, 
				colors=color, 
				shadow=False, 
				startangle=sangle,
				labels=legend if legend is not None else None)
	
	# set the title of img
	if title is not None:
		ax.set_title(title)
	# set the X-Y label of img
	if xlabel is not None:
		ax.set_xlabel(xlabel)
	if ylabel is not None:
		ax.set_ylabel(ylabel)

	plt.axis('equal')
	plt.tight_layout()
	plt.show()


# draw the histogram 
def hist_plot():
	pass

# draw the dot chart
def dot_plot():
	pass


# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# pie_plot(sizes, color=colors, text=True, title="Title", xlabel="XXX", ylabel="YYY")

# data = [[90, 55, 40, 65], [85, 62, 54, 20]]
# grplabel=['A', 'B', 'C', 'D']
# legend=["Frank", "Jerry"]
# bar_plot(data, grplabel=grplabel, color=colors, legend=legend, text=True, onavg=True, xlabel="XXX", ylabel="YYY", title="Title")

# s = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
# line_plot(s, legend=["JAL","ANA"],xlabel="XXX", ylabel="YYY", title="Title",color=colors, mark=["s","x","D","|"])
