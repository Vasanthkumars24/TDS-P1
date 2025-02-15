from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def execute_task_a9():
    with open("/data/comments.txt", "r") as file:
        comments = file.readlines()

    # Load a pre-trained embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings for all comments
    embeddings = model.encode(comments)

    # Compute pairwise cosine similarity
    similarity_matrix = cosine_similarity(embeddings)

    # Find the most similar pair (excluding self-similarity)
    most_similar_pair = None
    max_similarity = -1
    for i in range(len(comments)):
        for j in range(i + 1, len(comments)):
            if similarity_matrix[i][j] > max_similarity:
                max_similarity = similarity_matrix[i][j]
                most_similar_pair = (comments[i].strip(), comments[j].strip())

    # Write the most similar pair to a new file
    with open("/data/comments-similar.txt", "w") as file:
        file.write("\n".join(most_similar_pair))
