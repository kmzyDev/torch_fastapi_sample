import torch

from schemas import InputParams

def hoge(request: InputParams) -> str:
    # 循環参照回避のためここでmainの名前空間から引き込む
    from main import tokenizer, model, device
    prompt = tokenizer(request.prompt, return_tensors='pt').to(device)

    with torch.no_grad():
        outputs = model.generate(prompt['input_ids'], max_length=100)

    # 文字列長よりトークン長で切った方が良い説がある...
    return tokenizer.decode(outputs[0], skip_special_tokens=True)[len(request.prompt):].strip()
