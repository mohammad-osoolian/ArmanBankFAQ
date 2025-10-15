import pandas as pd

faqs = pd.read_csv('faqs.csv')
tfaqs = pd.read_json('batches/results.jsonl', lines=True)

id_to_class = faqs.set_index('id')['class'].to_dict()

tfaqs['class'] = tfaqs['id'].map(id_to_class)

tfaqs['id'] = range(len(tfaqs))

tfaqs.to_json('farsi-bank-faqs.jsonl', lines=True, orient='records', force_ascii=False)

class_counts = tfaqs.groupby('class').size()

# Optional: sort descending
class_counts = class_counts.sort_values(ascending=False)

print(class_counts)