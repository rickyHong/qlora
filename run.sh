# Good, GPU Memory < 8GB
#python3 qlora.py --model_name_or_path=EleutherAI/polyglot-ko-5.8b --dataset=alpaca-ko-01 --load_in_4bit=True --bnb_4bit_compute_dtype=torch.bfloat16 --bnb_4bit_use_double_quant=True --bnb_4bit_quant_type='nf4'
# Good, GPU Memory < 8GB
#python3 qlora.py --model_name_or_path=EleutherAI/polyglot-ko-5.8b --dataset=alpaca-ko-02 --load_in_4bit=True --bnb_4bit_compute_dtype=torch.bfloat16 --bnb_4bit_use_double_quant=True --bnb_4bit_quant_type='nf4'
# Good, GPU Memory < 12GB
python3 qlora.py --model_name_or_path=EleutherAI/polyglot-ko-12.8b --dataset=alpaca-ko-01 --load_in_4bit=True --bnb_4bit_compute_dtype=torch.bfloat16 --bnb_4bit_use_double_quant=True --bnb_4bit_quant_type='nf4'
