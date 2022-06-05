import gzip
import csv

blocks_csv = csv.writer(open('../Data/ImportData/Recipients.csv', 'w'))
header = ['recipient_id:ID',':LABEL']
blocks_csv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Inputs/blockchair_bitcoin_inputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[6], "Recipient"]
            blocks_csv.writerow(row)

for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Outputs/blockchair_bitcoin_outputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[6], "Recipient"]
            blocks_csv.writerow(row)