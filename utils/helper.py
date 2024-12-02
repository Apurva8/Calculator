import yaml
import csv

def load_yaml(config_file: str):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def read_csv(csv_file: str):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        rows = list(reader)  
    return rows, headers

def write_csv(results,headers,output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {output_file}")