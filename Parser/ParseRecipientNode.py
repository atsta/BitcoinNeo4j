import gzip
import csv

recipient_ids = []
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Outputs/blockchair_bitcoin_outputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            recipient_id = fields[6]
            recipient_ids.append(recipient_id)

for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Inputs/blockchair_bitcoin_inputs_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            recipient_id = fields[6]
            recipient_ids.append(recipient_id)

# recipient_ids_unique = []
# for recipient_id in recipient_ids:
#     if recipient_id not in recipient_ids_unique:
#         recipient_ids_unique.append(recipient_id)

recipient_ids_set= set(recipient_ids)
recipient_ids_unique = (list(recipient_ids_set))

importcsv = csv.writer(open('../Data/ImportData/Recipients.csv', 'w'))
header = ['recipient_id:ID',':LABEL']
importcsv.writerow(header)
for recipient_id in recipient_ids_unique:
    row = [recipient_id, "Recipient"]
    importcsv.writerow(row)