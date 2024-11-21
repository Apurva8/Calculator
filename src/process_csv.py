from utils import helper

def process_operations_from_csv(csv_file: str, mappings: dict):
    print("Mappings:", mappings)  
    rows = helper.read_csv(csv_file)

    for row in rows:
        print("Processing row:", row)  
        operation = row['operation']
        operand1 = int(row['operand1'])
        operand2 = int(row['operand2'])

        # if operation not in mappings:
        #     print(f"Unknown operation: {operation}")
        #     continue

        func = mappings[operation]
        try:#dont haandle unknown errors
            result = func(operand1, operand2)
            print(f"{operation.capitalize()} of {operand1} and {operand2} = {result}")
        except Exception as e:
            print(f"Error performing {operation}: {e}")
