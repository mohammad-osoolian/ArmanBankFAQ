import json
import pandas as pd
from openai import OpenAI


def write_batch(id, batch):
    joined = "\n".join([f"ID: {sample_id}\nQ: {q}\nA: {a}" for (sample_id, q, a) in batch])
    sysp = """پرسش و پاسخ های انگلیسی زیر رو به فارسی محاوره ای تبدیل کن. حواست باشه که:
    1- فارسی محاوره ای باشه
    2- تمام کلمات انگلیسی شامل اسامی خاص مخفف ها اصلاحات بانکی همگی به فارسی تبدیل شوند.
    3- هیچ کلمه یا حرف انگلیسی ای در ترجمه نباشه
    
    Return strictly as JSONL: {'id': ..., 'Q': '...', 'A': '...'}"""        

    with open(batch_dir + f"batch_{id}.txt", 'w') as f:
        f.write(sysp + '\n\n' + joined)

df = pd.read_csv('faqs.csv')[0:100]


batch_dir = 'batches/'
batch_size = 20

for i in range(0, len(df), batch_size):
    batch_pairs_with_id = df[["id", "question", "answer"]].iloc[i:i+batch_size].values.tolist()
    batch_translations = write_batch(i // batch_size, batch_pairs_with_id)

