import jsonlines
extracted_records=[]
with jsonlines.open('ch.txt') as reader:
    for obj in reader:
        x=obj["url"]
        print(x);
        record = {
        'url':x}
        extracted_records.append(record)
with jsonlines.open('outp.txt', mode='w') as writer:
    writer.write(extracted_records)
