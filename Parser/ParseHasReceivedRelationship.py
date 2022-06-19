import gzip
import csv

importcsv = csv.writer(open('../Data/ImportData/Outputs.csv', 'w'))
header = [':START_ID','time','value:float','value_usd:float','type','is_spendable',':END_ID',':TYPE']
importcsv.writerow(header)
for i in range(10,21): 
    print(i)
    current_time = ""
    current_recipient= ""
    current_transactions = ""
    with gzip.open('../Data/Outputs/blockchair_bitcoin_outputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            if fields[3] == current_time and fields[6] == current_recipient and fields[1] == current_transaction:
                continue
            current_time = fields[3]
            current_recipient = fields[6]
            current_transaction = fields[1]
            row = [current_transaction, current_time, fields[4], fields[5], fields[7], fields[10], current_recipient, "HAS_RECEIVED"]
            importcsv.writerow(row)