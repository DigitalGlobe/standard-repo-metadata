import sys
import yaml
from jsonschema import validate as jsonschema_validate


def main(args):
	# Handle input arguments
	arg_syntax = "python schema_validator.py schema_filepath input_filepath"

	schema_filepath = args[0]
	data_filepath = args[1]

	with open(data_filepath) as f:
		data = yaml.load(f.read())

	with open(schema_filepath) as f:
		yaml_schema = yaml.load(f.read())

	jsonschema_validate(data, yaml_schema)
	
	print("Your YAML file is compliant with the schema!")


if __name__ == "__main__":
	main(sys.argv[1:])