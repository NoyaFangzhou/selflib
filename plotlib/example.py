#!/usr/bin/python
import plotlib as pl

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
pl.pie_plot(sizes, color=colors, text=True, title="Title", xlabel="XXX", ylabel="YYY")

data = [[90, 55, 40, 65], [85, 62, 54, 20]]
grplabel=['A', 'B', 'C', 'D']
legend=["CLASS 1", "CLASS 3"]
pl.bar_plot(data, grplabel=grplabel, color=colors, legend=legend, text=True, onavg=True, xlabel="XXX", ylabel="YYY", title="Title")

s = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]
pl.line_plot(s, legend=["Air China","All Nippon Airways"],xlabel="XXX", ylabel="YYY", title="Title",color=colors, mark=["s","x","D","|"])