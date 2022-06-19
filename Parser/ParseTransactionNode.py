import gzip
import csv

importcsv = csv.writer(open('../Data/ImportData/Transactions.csv', 'w'))
header = ['hash:ID','time','size:int','weight:int','is_coinbase','has_witness','input_total:float','input_total_usd:float','output_total:float','output_total_usd:float','fee:float','fee_usd:float','fee_per_kwu:float','fee_per_kwu_usd:float',':LABEL']
importcsv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Transactions/blockchair_bitcoin_transactions_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[1], fields[2], fields[3], fields[4], fields[7], fields[8], fields[11], fields[12], fields[13], fields[14], fields[15], fields[16], fields[19], fields[20], "Transaction"]
            importcsv.writerow(row)