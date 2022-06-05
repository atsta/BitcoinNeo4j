import gzip
import csv

blocks_csv = csv.writer(open('../Data/Outputs.csv', 'w'))
header = [':START_ID','time','value','value_usd','type','is_spendable',':END_ID',':TYPE']
blocks_csv.writerow(header)
for i in range(10,31): 
    print(i)
    with gzip.open('../Data/Outputs/blockchair_bitcoin_outputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[1], fields[3], fields[4], fields[5], fields[7], fields[10], fields[6], "HAS_RECEIVED"]
            blocks_csv.writerow(row)