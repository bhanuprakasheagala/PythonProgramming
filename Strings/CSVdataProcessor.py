import csv

def process_csv(file_path, column_name):
  values = []

  try:
    with open(file_path, 'r', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        try:
          value = float(row[column_name])
          values.append(value)
        except ValueError:
          continue
    if values:
      avg = sum(values)/len(values)
      with open('avg_results.txt', 'w') as result_file:
        result_file.write(f"Average value for '{column_name}':{avg:.2f}\n")

      print("CSV processing complete. Results saved to avg_results.txt.")
    else:
      print("No valid data found in the specified column.")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  csv_file = 'data.csv'
  column = 'Value'
  process_csv(csv_file, column)
  
