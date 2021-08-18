import numpy as np

def makePOSCAR(filename, p, cellparameters, spe, nums):
	with open(filename, 'w') as f:
		f.write("POSCAR\n")
		f.write("1.0000000\n")
		for v in cellparameters:
			for x in v:
				f.write("%13.8f"%x)
			f.write("\n")

		f.write(" ".join(spe))
		f.write("\n")
		str_nums = [str(num) for num in nums]
		f.write(" ".join(nums))
		f.write("\n")
		f.write("Direct\n")
		for v in p:
			for x in v:
				f.write("%13.8f"%x)
			f.write("\n")

def interpolation(p1, p2, N, tag, cellparameters, spe, nums):
	dis = p2 - p1
	q = dis/(N+1)
	for i in range(N+2):
		makePOSCAR(tag+str(i)+ ".vasp", p1+q*i, cellparameters, spe, nums)
	for i in range(1, N+2):
		makePOSCAR(tag+"-"+str(i)+ ".vasp", p1-q*i, cellparameters, spe, nums)
