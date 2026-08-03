import openai
import yaml
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_yaml(instruction_text):
    prompt = f"""
Extract structured data from the following RISC-V instruction.

Return ONLY valid YAML

instruction:
{instruction_text}

format:
instruction: <name>
operation: <operation style>
operands: <number>
type: <category>
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}],
        temperature=0
    )
    output = response['choice'][0]['message']['content']
    return output

def validate_yaml(yaml_text):
    try:
        data = yaml.safe_load(yaml_text)
        return True, data
    except Exception as e:
        return False, str(e)