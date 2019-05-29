# Read from the file file.txt and output the tenth line to stdout.
awk 'NR==10{print $0}' file.txt

#W2
# Read from the file file.txt and output the tenth line to stdout.
awk '{if(NR == 10) {print $0}}' file.txt