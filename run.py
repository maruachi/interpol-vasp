import sys
from .scr.core import *
from .scr.read import *

sys.path.append('/home/maruachi/Research_project/3_Dimer_models/interpol-vasp')

if len(sys.argv) == 1:
	print("tail1 tail2 N tag")
	sys.exit()

ftail1 = sys.argv[1]
ftail2 = sys.argv[2]
N = int(sys.argv[3])
tag = sys.argv[4]

cellparameters, spe, nums = read_head(ftail1)
p1 = read_atoms(ftail1)
p2 = read_atoms(ftail2)
interpolation(p1, p2, N, tag, cellparameters, spe, nums)
