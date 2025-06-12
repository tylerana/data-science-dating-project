import torch
from transformers import AutoTokenizer, AutoModel
import os
import glob
from torch.utils.data import DataLoader
import torch.nn.functional as F
import warnings

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name).to(device)

warnings.filterwarnings('ignore')


def embed_user_essay(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
    
    with torch.no_grad():
        outputs = model(**inputs)
        
    # mean pooling
    token_embeddings = outputs.last_hidden_state
    attention_mask = inputs['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()
    pooled = torch.sum(token_embeddings * attention_mask, dim = 1) / torch.clamp(attention_mask.sum(1), min=1e-9)
    
    # normalizing
    embedding = F.normalize(pooled, p=2, dim=1)
    
    return embedding.cpu().numpy().flatten()