import re
import numpy as np

def read_head(filename):
	cellparameters = []
	spe = []
	nums = []
	with open(filename, "r") as f:
		f.readline()
		f.readline()
		for _ in range(3):
			line = f.readline()
			v = re.findall("[+-]?[0-9]+\.[0-9]+", line)
			v = [float(x) for x in v]
			cellparameters.append(v)

		line = f.readline()
		spe = re.findall("[A-Za-z]+", line)
		line = f.readline()
		nums = re.findall("[0-9]+", line)
	return np.array(cellparameters), spe, nums

def read_atoms(filename):
	atoms = []
	with open(filename, "r") as f:
		for _ in range(8):
			f.readline()

		for line in f:
			v = re.findall("[+-]?[0-9]+\.[0-9]+", line)
			v = [float(x) for x in v]
			atoms.append(v)
	
	return np.array(atoms)
