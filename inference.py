import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

#model_name = "huggyllama/llama-7b"
#adapters_name = 'timdettmers/guanaco-7b'
model_name = "EleutherAI/polyglot-ko-1.3b"
adapters_name = 'output/output13b/adapter_model'

# for 16bit
"""
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_memory= {i: '24000MB' for i in range(torch.cuda.device_count())},
)
model = PeftModel.from_pretrained(model, adapters_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
"""

#for 4bit
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    max_memory= {i: '24000MB' for i in range(torch.cuda.device_count())},
    quantization_config=BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type='nf4'
    ),
)
model = PeftModel.from_pretrained(
        model,
        adapters_name,
        #local_files_only=True
        )

tokenizer = AutoTokenizer.from_pretrained(model_name)

while True:
    prompt = input(f'Human:')
    formatted_prompt = (
        f"### Human: {prompt} ### Assistant:"
)

    inputs = tokenizer(formatted_prompt, return_tensors="pt").to("cuda:0")
    outputs = model.generate(inputs=inputs.input_ids, max_new_tokens=2000)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
