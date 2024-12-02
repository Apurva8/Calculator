from src import operations_map
from utils import helper

def create_dynamic_mapping(config_file):
    config = helper.load_yaml(config_file) 
    operations_config = config.get('operations', {})
    
    dynamic_operation_map = {}
    for op_name, func_name in operations_config.items():
        if func_name in operations_map.operation_map:  
            dynamic_operation_map[op_name] = operations_map.operation_map[func_name]  
        else:
            print(f"Warning: Function '{func_name}' is not defined.")
    return dynamic_operation_map

 