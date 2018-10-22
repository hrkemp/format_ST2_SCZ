##################################################

### script: format_ST2_SCZ.py
### ran on python release: Python 3.6
### author: Harriet Kemp

### version: 1.0.0
### version birth: 22.10.2018
### most recent version modificaton: 22.10.2018

### run like: format_ST2_SCZ.py

##################################################

import sys,re,os,math

inputfile = "/Users/hkemp2/Documents/scripts/test/SWGPGC_ST2.txt"
outputfile_all = "/Users/hkemp2/Documents/scripts/test/SWGPGC_ST2_formatted.tsv"
outputfile_chr12 = "/Users/hkemp2/Documents/scripts/test/SWGPGC_ST2_formatted_chr12.tsv"


def formatline (line):
	line = re.sub("\s+\(\S+\)", "", line)
	line = re.sub("\s+", "\t", line)
	line = re.sub("\,", "", line)
	bits = line.split("\t")
	return bits
	
def calcpvalscore (bits):
	pval = bits[8]
	score = 0
	if re.search("e-",pval):
		pbits = pval.split("e-")
		score = pbits[1]
		if re.search("\.",pval):
			nbits = pval.split(".")
			ded = 10-int(nbits[0])
			score = str(score) + "." + str(ded)
		else:
			ded = 10-int(pbits[0])
			score = str(score) + "." + str(ded)
	else:
		if re.search("\.",pval):
			pbits = pval.split(".")
			score = len(str(pbits[1]))+1
			ded = 10-int(pbiys[0])
			score = str(score) + "." + str(ded)
		if pval == 1:
			score = 0.1
	return score

def sumpvalscores(inputfile):
	file = open(inputfile,"r")
	total = 0
	for line in file:
		if re.search("\(",line):
			bits = formatline(line)
			score = calcpvalscore(bits)
			total += float(score)
			print ("pval = ",bits[8],"     score = ",score)
	return total

### calculate sum of pvalue scores for weighting
total = sumpvalscores(inputfile)
print ("TOTAL = ",total)

### print newly formatted lines to output file
file = open(inputfile,"r")
svall = open(outputfile_all,"w")
svchr12 = open(outputfile_chr12,"w")
(n,n12) = (0,0)
for line in file:
	if re.search("\(",line):
		bits = formatline(line)
		score = calcpvalscore(bits)
		weight = math.ceil(float(score)/int(total)*100000)/100000
		if re.search('\d+',bits[2]):
#			print ("alls.group(1) = ",bits[2])
			continue
		else:
#			line = re.sub("\,", "", line)
			coords = bits[6].split("-")
			for i in range(int(coords[0]),int(coords[1])):
				n = n+1
				nwline = bits[0] + "\t" + bits[1] + "\t" + bits[2] + "\t" + bits[5] + "\t" + str(i) + "\t" + bits[8] + "\t" + str(score) + "\t" + str(weight) + "\n"
				svall.write(nwline)
				if bits[5] == 12:
					n12 = n12+1
					svchr12.write(nwline)
	#				print (nwline)
	else:
		line = re.sub("\s+", "\t", line)
		tbits = line.split("\t")
		ntline = tbits[0] + "\t" + tbits[1] + "\t" + tbits[2] + "\t" + tbits[5] + "\tPosition\t" + tbits[8] + "\tpval_score\tpval_weight\n"
		svall.write(ntline)
		svchr12.write(ntline)
#	n = n+1
#	if n == 3:
#		sys.exit()

svall.close()

print ("\nn = ",n,"\n")
print ("\nn12 = ",n12,"\n")
