#!usr/bin/python
import os

def read_from_file(file, path=".", accp="r"):
	assert file is not None, "Error! No filename given"
	fname = "{}/{}".format(path, file)
	fp = open(fname, accp)
	lines = [l for l in (line.strip() for line in fp) if l]
	content = []
	for line in lines:
		content.append(line)
	fp.close()
	return content




def write_to_file(file, content, path=".", accp="a"):
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
			write_to_file(file, content[k], path=path, accp=accp)

	fp.close()
