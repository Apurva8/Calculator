from src import operations_loader
from src import process_csv
import os


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "configurations", "config.yaml")
    csv_path = os.path.join(base_dir, "data", "data.csv")
    config_path_relative = os.path.relpath(config_path, os.getcwd())
    csv_path_relative = os.path.relpath(csv_path, os.getcwd())
    
    mappings = operations_loader.create_dynamic_mapping(config_path_relative)
    process_csv.process_operations_from_csv(csv_path_relative, mappings)

if __name__ == '__main__':
    main()
