from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from routers import router

app = FastAPI()

model_name = '../assets/l3-elyza'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
device = torch.device('cuda')
model.to(device)

app.include_router(router)
