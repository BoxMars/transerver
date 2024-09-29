import argparse
import toml
from rich import print
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

from flask import Flask, request, jsonify

app=Flask('transerver')

parser = argparse.ArgumentParser(
    prog='transerver',
    description='A server for interacting LLM model locally with OpenAI style API using transformers',
    )

parser.add_argument(
    '-c', '--config', required=True, help='Path to the config file',
)

args=parser.parse_args()

print(f"Config file: {args.config}")
config=toml.load(args.config)

model_path=config['model']['model']
    
print(f"Loading model from {model_path}")
model=AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer=AutoTokenizer.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto")
pipe=pipeline('text-generation', model=model, tokenizer=tokenizer, torch_dtype=torch.bfloat16, device_map="auto")

@app.route('/v1/chat/completions', methods=['POST'])
def completion():
    data=request.json
    messgae=data['messages']
    
    response=pipe(messgae, max_new_tokens=200, temperature=0.2)

    new_message=response[0]['generated_text'][-1]


    return jsonify({
        'choices':[
            {'index':0,
            'message':new_message}
        ]
    })    
    
def main():
    
    host=config['server']['host']
    prot=config['server']['port']
    
    print(f"Starting server at {host}:{prot}")
    
    app.run(host=host, port=prot)
    
    
    
if __name__ == "__main__":
    main()