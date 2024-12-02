from configurations import path_configurations
from src import operations_loader
from utils import helper


def save_results_to_csv(rows_to_save, output_headers, output_file):
    helper.write_csv(rows_to_save, output_headers, output_file)

def display_results(rows_to_display):
    for results in rows_to_display:
        print(
            f"{results['operation'].capitalize()} of {results['operand1']} and {results['operand2']} = {results['results']}"
        )

def ensure_results_header(headers):
    if "results" not in headers:
        headers.append("results")
    return headers

def split_rows_by_output_mode(results):
    rows_to_save = [row for row in results if row.get('output_mode') == 'save']
    rows_to_display = [row for row in results if row.get('output_mode', 'print') != 'save']
    return rows_to_save, rows_to_display

def handle_output(context, output_file):
    results = context['results']
    headers = context['headers']

    rows_to_save, rows_to_display = split_rows_by_output_mode (results)
    updated_headers = ensure_results_header(headers)
    if rows_to_display:
        display_results(rows_to_display)
    if rows_to_save:
        save_results_to_csv(rows_to_save, updated_headers, output_file)

def compute_result(row, mappings):
    operation = row['operation']
    operand1 = int(row['operand1'])
    operand2 = int(row['operand2'])
    func = mappings[operation]
    return func(operand1, operand2)

def process_functions(context):
    rows = context.get('rows', [])
    context['results'] = [{**row, 'results': compute_result(row, context['mappings'])} for row in rows]
    return context


def read_input_data(csv_data_path):
    return helper.read_csv(csv_data_path)

def build_context(context):
    context['mappings'] = operations_loader.create_dynamic_mapping(context['configurations'].yaml_file_path)
    rows,headers = read_input_data(context['configurations'].csv_file_path)
    context['rows'] = rows
    context['headers'] = headers
    return context

def process_data_pipeline():
    context = {}
    context['configurations'] = path_configurations
    context = build_context(context)
    context = process_functions(context)
    handle_output(context, context['configurations'].output_file_path)