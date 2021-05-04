import re

outfile = open('/home/yinuo/bds/shadowhand/ngrams_only_stock.csv', 'w')
l = "ngram,sentiment\n"
outfile.write(l)

rule = re.compile(r'^(?!-)')
with open('/home/yinuo/bds/shadowhand/stocks.txt', 'r') as fp:
    line = fp.readline()
    while line:
        if rule.match(line):
            print(line)
            line = (line.split(":"))[0] + "\n"
            outfile.write(line)
        line = fp.readline()

outfile.close()
        

