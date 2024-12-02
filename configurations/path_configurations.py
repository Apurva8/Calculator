import os 

base_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(base_dir, os.pardir))

csv_file_path = os.path.join(root_dir, "data", "data.csv")
yaml_file_path = os.path.join(root_dir, "configurations", "config.yaml")
output_file_path = os.path.join(root_dir, "data", "output_results.csv")