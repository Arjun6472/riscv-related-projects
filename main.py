from extractor import extract_yaml, validate_yaml

def run():
    print("RISC-V YAML Extractor")

    instruction = input("Enter instruction description \n")

    yaml_output = extract_yaml(instruction)

    print("\n Genrated YAML:\n")
    print(yaml_output)

    valid, result = validate_yaml(yaml_output)

    if valid:
        print("\n </ YAML is valid")
        print(result)
        
    else:
        print("\n YAML Error:", result)


if __name__=="__main__":
    run()