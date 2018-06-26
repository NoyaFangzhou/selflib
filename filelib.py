#!usr/bin/python
import os

def read_from_file(path=".", file, accp="r"):
	assert file is not None, "Error! No filename given"
	fname = "{}/{}".format(path, file)
	fp = open(fname, accp)
	lines = [l for l in (line.strip() for line in fp) if lp]
	content = []
	for line in lines:
		content.append(line)
	fp.close()
	return content




def write_to_file(path=".", file, content, accp="a"):
	assert file is not None, "Error! No filename given"
	assert content is not None, "Error! No content can be written in file"
	fname = "{}/{}".format(path, file)
	fp = open(fname, accp)
	if type(content) is list:
		for l in content:
			fp.write(l+"\n")
	elif type(content) is str:
		fp.write(content+"\n")
	elif type(content) is dict:
		for k in content.keys():
			fp.write(k+"\t")
			write_to_file(path=path, file, content[k], accp=accp)

	fp.close()