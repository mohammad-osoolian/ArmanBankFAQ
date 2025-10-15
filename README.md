**This report contains detailed information and statistics for each approach, as well as the steps taken before reaching the final model, such as model selection and fine-tuning. For the final results, check `Compare.ipynb` notebook and `Ka-ChatBot_BenchMark.xlsx` file**  

# Contents
- STS Approach
    - Model Selection
    - Predictions Analysis
    - Data Generation
    - Domain Specification
- LLM Approach
    - Model Selection
- Comparison of Two Approaches

# STS Approach
In this approach, first I explored sentence-transformer models for Farsi and tested their performance. Then I selected the best model and, after analyzing its performance, decided to fine-tune it with domain-specific data. I used a Bank FAQs dataset, translated it into Farsi, and then fine-tuned the sentence transformer with it.

## Model Selection

- Notebook: `notebooks/sentence-transformer/overall-check.ipynb`
- Predictions csv file: `notebooks/sentence-transformer/results.csv`

| Model Name                              | Score |
|------------------------------------------|--------|
| PartAI/Tooka-SBERT-V2-Large              | 0.753  |
| xmanii/maux-gte-persian                  | 0.720  |
| BAAI/bge-m3                              | 0.720  |
| intfloat/multilingual-e5-base            | 0.645  |
| sentence-transformers/LaBSE              | 0.462  |
| google/embeddinggemma-300m               | 0.301  |

*results of the tested models on the Arman FAQs dataset (the given dataset)*


## Predictions Analysis

- Notebook: `notebooks/sentence-transformer/predictions_analysis.ipynb`

| Accuracy | Value |
|---------|--------|
| Top-1   | 0.753  |
| Top-2   | 0.882  |
| Top-3   | 0.914  |
| Top-5   | 0.935  |
| Top-10  | 0.957  |

*Top-k accuracy.*

| Avg Margin | Value  |
|-------------------------------|--------|
| Correct Predictions           | 0.104  |
| Wrong Predictions             | 0.032  |

*Average margin of similarity scores between the first and second predictions for correct and incorrect predictions.*

| Metric                                | Value |
|---------------------------------------|--------|
| Category Prediction Accuracy          | 0.828  |

*Accuracy of predicting the correct category.*

## Data Generation
First, I translated an English Bank FAQ dataset into Farsi using ChatGPT-4 (web interface):

- Source dataset: [Bank FAQs](https://www.kaggle.com/datasets/somanathkshirasagar/bankfaqs)  
- Data generation notebooks: `data-generation/*`  
- Translated data: `data-generation/farsi-bank-faqs.jsonl`  

## Domain Specification
Then I fine-tuned PartAI/Tooka-SBERT-V2-Large on this data:

- Notebook: `notebooks/sentence-transformer/fine_tune.ipynb`  

| Parameter               | Value |
|--------------------------|--------|
| Base Model               | PartAI/Tooka-SBERT-V2-Large |
| Dataset                  | farsi-bank-faqs |
| Finetuned Model          | mohammad-osoolian/arman-tooka2-finetuned |
| Epochs                   | 1 |
| Learning Rate (lr)       | $1e-5$ |
| Accuracy (before fine-tune) | 0.753 |
| Accuracy (after fine-tune)  | 0.817 |

*Model fine-tuning information.*

# LLM Approach
For this approach, I explored recent models with fewer than 8B parameters and tested their performance on the Arman FAQ dataset.

- Notebooks: `notebooks/LLM/Inferences/*`
- Predictions csv file: `notebooks/LLM/results.csv`

## Model Selection 

| Model                        | Accuracy | Error Parsing JSON |
|-------------------------------|---------|------------------|
| LLama-3-8b-instruct           | 0.752   | 0.011             |
| Mistral-7b-instruct-v0.3      | 0.569   | 0                |
| Qwen3-4b-instruct-2507        | 0.828   | 0                |
| Gemma-3-4b-it|                | 0.623    | 0              |

*Check each model’s notebook for instructions and system prompts.*

# Comparison of Two Approaches
Check `Compare.ipynb`. The notebook itself is complete and clear. Also Final results are added in `Ka-ChatBot_BenchMark.xlsx`.
