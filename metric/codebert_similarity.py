from transformers import RobertaTokenizer, RobertaModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")

def get_embedding(code):
    inputs = tokenizer(code, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach()

emb1 = get_embedding("if action == \"add\" and form.is_submitted():")
emb2 = get_embedding("if action == 'add' and form.is_submitted():")

score = cosine_similarity(emb1.numpy(), emb2.numpy())
print(score[0][0])  # 越接近1越相似