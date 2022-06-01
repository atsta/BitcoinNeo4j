import gzip
import csv

blocks_csv = csv.writer(open('../Data/Rewards.csv', 'w'))
header = [':START_ID','reward','reward_usd',':END_ID',':TYPE']
blocks_csv.writerow(header)
for i in range(10,31): 
    print(i)
    with gzip.open('../Data/Blocks/blockchair_bitcoin_blocks_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            #blockId, reward, reward_usd, guessed_miner
            row = [fields[0], fields[-3], fields[-2], fields[-1], "REWARDED"]
            blocks_csv.writerow(row)