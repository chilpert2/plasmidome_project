import sys 

def usage(): 
	print("Format krona tsv file generate by bash commands to a proper krona txt file for graphic generation") 
	print("---") 
	print("usage: python3 krona_txt.py <krona tsv input file> <krona txt output file>") 
	print("---")
	print("krona tsv file is a file generate by sort and uniq -c command (ex : cut -f 3- summary_plasmids.tsv | sort | uniq -c) with lines like : 14 Archaea	Crenarchaeota	Thermoprotei	Sulfolobales	Sulfolobaceae	Sulfolobus	Sulfolobus islandicus") 
	print("14 is the number of sequence with this taxonomic lineage and rest of the line is taxonomic lineage")     

if len(sys.argv) != 3:
	usage() 
	exit() 

f=open(sys.argv[1]) 

out=open(sys.argv[2],"w") 

for l in f : 
	l_split=l.lstrip().rstrip().split(" ")
	number=l_split[0]
	tax=" ".join(l_split[1:])
	out.write(number+"\t"+tax+"\n") 
out.close() 	