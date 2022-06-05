import gzip
import csv

importcsv = csv.writer(open('../Data/ImportData/Rewards.csv', 'w'))
header = [':START_ID','reward','reward_usd',':END_ID',':TYPE']
importcsv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Blocks/blockchair_bitcoin_blocks_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[0], fields[-3], fields[-2], fields[-1], "REWARDED"]
            importcsv.writerow(row)