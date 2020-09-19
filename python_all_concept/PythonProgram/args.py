import argparse
parser=argparse.ArgumentParser()
parser.add_argument("square",help="this is a square",type=int)
parser.add_argument("--database",help="this is a database",type=str)
parser.add_argument("cube",help="this is a cube",type=int)
args=parser.parse_args()
var1=args.square**2
var2=args.cube**3
if args.database>=str(2):
	var3="connected"
else:
	var3="not connected"
		
print("square is {},cube is {},database is {}".format(var1,var2,var3))





