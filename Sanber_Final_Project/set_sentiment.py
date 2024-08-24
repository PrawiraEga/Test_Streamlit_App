# Hitung Durasi Proses
import time
from datetime import timedelta
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, BertTokenizer, BertForSequenceClassification

txt = "liquidity crisis causes major price slippage cryptocurrency sell offs kaiko"

def calculate_process_time(start_time):
  """Calculates the process time in hh:mm:ss format.

  Args:
    start_time: The start time of the process as a float representing seconds since
                the epoch.

  Returns:
    A string representing the process time in hh:mm:ss format.
  """

  end_time = time.time()
  elapsed_time = end_time - start_time
  elapsed_time_delta = timedelta(seconds=elapsed_time)
  process_time_str = str(elapsed_time_delta)

  # Extract hh:mm:ss from the timedelta string
  hours, minutes, seconds = process_time_str.split(':')
  return f"{hours}:{minutes}:{seconds}"

# Method Transformer Specific Model
def set_sentiment_spec(text):
  # 1. Load pre-trained model dan tokenizer
  fin_model = "marcev/financebert"
#   fin_model = "ahmedrachid/FinancialBERT-Sentiment-Analysis"
  tokenizer = AutoTokenizer.from_pretrained(fin_model)
  model = AutoModelForSequenceClassification.from_pretrained(fin_model)

# 2. Membuat pipeline untuk text classification
  classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# 3. Contoh teks yang akan diklasifikasikan
  texts = txt

# 4. Prediksi kelas dan mendapatkan skor
  results = classifier(texts)
  return results

print("=== Transformer Specific Model ===")
print(txt)

start_time = time.time()

sentiment = set_sentiment_spec(txt)

#durasi
process_time = calculate_process_time(start_time)
print("Process time:", process_time)

print(sentiment)