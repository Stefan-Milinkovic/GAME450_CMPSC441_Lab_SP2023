from sentence_transformers import SentenceTransformer, util
sentences = ["Meaning of life is subjective and varies for each individual.", "Meaning of life: subjective, varies, purposeful, individual, fulfilling, subjective."]
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

embedding_1 = model.encode(sentences[0], convert_to_tensor=True)
embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

score = util.pytorch_cos_sim(embedding_1, embedding_2)
print(score)

# score = .8938. Multiplying by 100 gives 89.38, which I will use as a percentage of how similar the answers are.
# score = 89.38% similarity