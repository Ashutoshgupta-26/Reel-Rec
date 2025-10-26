# embeddings_task.py
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Step 1: Load Pretrained Model ----------
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# ---------- Step 2: Create Sample Reel Captions ----------
captions = [
    "Funny cat fails compilation",
    "Cooking tutorial: pasta carbonara",
    "Football skills and goals",
    "Python programming tips for beginners",
    "Cute kitten playing with yarn",
    "Delicious chocolate cake recipe",
    "Top 10 football tricks",
    "Learn Python loops and functions"
]

# ---------- Step 3: Create Function to Generate Embeddings ----------
def get_embeddings(text_list):
    inputs = tokenizer(text_list, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)  # Average pooling
    return embeddings.numpy()

# Generate embeddings
embeddings = get_embeddings(captions)

# ---------- Step 4: Calculate Cosine Similarity ----------
similarity_matrix = cosine_similarity(embeddings)

# ---------- Step 5: Display Results ----------
print("=== Cosine Similarity Between Reel Captions ===")
print("\nCaption Index:")
for i, caption in enumerate(captions):
    print(f"{i}: {caption}")

print(f"\nSimilarity Matrix (rounded to 2 decimal places):")
print(np.round(similarity_matrix, 2))

# ---------- Step 6: Find Most Similar Pairs ----------
n = len(captions)
pairs = []

# Collect all pairs with their similarity scores
for i in range(n):
    for j in range(i + 1, n):
        pairs.append((i, j, similarity_matrix[i][j]))

# Sort by similarity score (highest first)
pairs.sort(key=lambda x: x[2], reverse=True)

print("\n=== TOP SIMILAR REEL PAIRS ===")
for i, (idx1, idx2, score) in enumerate(pairs[:3]):
    print(f"\n{i+1}. Similarity Score: {score:.2f}")
    print(f"   '{captions[idx1]}'")
    print(f"   '{captions[idx2]}'")

print(f"\n=== ANALYSIS ===")
print(f"Total captions analyzed: {n}")
print(f"Embedding dimensions: {embeddings.shape[1]}")
print(f"Highest similarity: {pairs[0][2]:.2f}")
print(f"Lowest similarity: {pairs[-1][2]:.2f}")
print(f"Average similarity: {np.mean([p[2] for p in pairs]):.2f}")