import gzip
import csv

importcsv = csv.writer(open('../Data/ImportData/Inputs.csv', 'w'))
header = [':START_ID','time','value:float','value_usd:float','type','is_spendable','spending_block_id', 'spending_transaction_hash', 'spending_time','spending_value_usd','lifespan',':END_ID',':TYPE']
importcsv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Inputs/blockchair_bitcoin_inputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[6], fields[3], fields[4], fields[5], fields[7], fields[10], fields[11], fields[12], fields[14], fields[15], fields[19], fields[1], "HAS_GIVEN"]
            importcsv.writerow(row)