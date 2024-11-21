import yaml
import csv

def load_yaml(config_file: str):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def read_csv(csv_file: str):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  
    return rows
