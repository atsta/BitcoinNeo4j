import gzip
import csv

blocks_csv = csv.writer(open('../Data/ImportData/Inputs.csv', 'w'))
header = [':START_ID','time','value','value_usd','type','is_spendable','spending_block_id','spending_transaction_hash','spending_time','spending_value_usd','lifespan',':END_ID',':TYPE']
blocks_csv.writerow(header)
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Inputs/blockchair_bitcoin_inputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[6], fields[3], fields[4], fields[5], fields[7], fields[9], fields[10], fields[11], fields[13], fields[14], fields[18], fields[1], "HAS_GIVEN"]
            blocks_csv.writerow(row)