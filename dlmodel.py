from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'elyza/Llama-3-ELYZA-JP-8B'
save_path = './assets/l3-elyza'

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
