import gzip
import csv

importcsv = csv.writer(open('../Data/ImportData/BelongsTo.csv', 'w'))
header = [':START_ID',':END_ID',':TYPE']
importcsv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Transactions/blockchair_bitcoin_transactions_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[1], fields[0], "BELONGS_TO"]
            importcsv.writerow(row)