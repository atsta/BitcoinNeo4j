import gzip
import csv

blocks_csv = csv.writer(open('../Data/Transactions.csv', 'w'))
header = ['hash:ID','time','size','weight','is_coinbase','has_witness','input_total','input_total_usd','output_total','output_total_usd','fee','fee_usd','fee_per_kwu','fee_per_kwu_usd',':LABEL']
blocks_csv.writerow(header)
for i in range(10,31): 
    print(i)
    with gzip.open('../Data/Transactions/blockchair_bitcoin_transactions_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[1], fields[2], fields[3], fields[4], fields[7], fields[8], fields[11], fields[12], fields[13], fields[14], fields[15], fields[16], fields[19], fields[20], "Transaction"]
            #print("%s,%s,%s,Block" % (fields[0], fields[1], fields[2]))
            blocks_csv.writerow(row)