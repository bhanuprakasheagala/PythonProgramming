from colleactions import Counter
import re

def count_word_frequency(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      text = file.read()
      words = re.findall(r'\w+', text.lower())
      word_counts = Counter(words)
      return word_counts
  except Exception as e:
    printf(f"Error reading file {file_path}: {e}")
    return {}


file_path = '\path\to\example.txt
wf = word_frequency(file_path)
print(wf)
