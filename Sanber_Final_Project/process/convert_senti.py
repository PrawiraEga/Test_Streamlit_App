# Method To Value
def senti_to_val(txt):
  if txt == 'POSITIVE':
    return 1
  elif txt == 'NEGATIVE':
    return -1
  else:
    return 0
  
# Method Total Senti To Label
def senti_to_label(txt):
  if txt > 0:
    return 'POSITIVE'
  elif txt < 0:
    return 'NEGATIVE'
  else:
    return 'NEUTRAL'
