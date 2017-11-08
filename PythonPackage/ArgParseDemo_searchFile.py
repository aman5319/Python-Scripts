import re , argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("word" , help="Specify the word to search")
	parser.add_argument("fname" , help = "enter the file name")
	args = parser.parse_args()
	
	lineNum = 0
	found =0
	with open(args.fname) as file:
		for line in file.readlines():
			line = line.strip("\n\r")
			lineNum += 1
			search_result= re.search(args.word , line , re.M|re.I)
			if search_result:
				print(str(lineNum)+" : "+line)
				found += 1
	if found  ==0:
		print("Not found ")

if __name__=="__main__":
	main()
