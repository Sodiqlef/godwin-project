import time
import random

from django.shortcuts import render
from django.http import JsonResponse

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge_base import knowledge_base, preferred_keywords, greeting_queries, failed_queries

# Create your views here.
period = int(time.strftime('%H'))

# Preprocess the knowledge base data
lemmatizer = WordNetLemmatizer()
preprocessed_data = []
for sentence in knowledge_base:
    tokens = word_tokenize(sentence.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    preprocessed_data.append(" ".join(lemmatized_tokens))

# Vectorize the preprocessed data
vectorizer = TfidfVectorizer()
knowledge_base_vectors = vectorizer.fit_transform(preprocessed_data)


# Function to generate a response given a user query
def generate_response(query):
    preprocessed_query = " ".join([lemmatizer.lemmatize(
        token) for token in word_tokenize(query.lower())])

    # Check if any word from user query is in the preferred keywords
    matching_keywords = [
        keyword for keyword in preferred_keywords if keyword in preprocessed_query]

    if len(matching_keywords) >= 1:
        # Preprocess the user's query and create a query vector
        query_vector = vectorizer.transform([preprocessed_query])

        # Calculate cosine similarity scores
        similarity_scores = cosine_similarity(
            query_vector, knowledge_base_vectors).flatten()

        for keyword in matching_keywords:
            try:
                keyword_index = preferred_keywords.index(keyword)
                # Adjust the weight as needed
                similarity_scores[keyword_index] += 0.1
            except ValueError:
                pass  # Keyword not found in preferred_keywords

        # Find the index of the first matching sentence in the knowledge base
        max_score = max(similarity_scores)
        if max_score > 0:
            most_similar_indices = [
                i for i, score in enumerate(similarity_scores) if score == max_score]
            first_matching_index = most_similar_indices[0]
            return knowledge_base[first_matching_index]

    # No matching keywords found, return default response
    return random.choice(failed_queries)


def home(request):
    return render(request, 'index.html')


def chatbot(request):
    if request.method == 'POST':
        user_query = request.POST.get("user_query")
        if user_query in greeting_queries:
            if period >= 0 and period < 12:
                response = "Good morning, I'm always here to help you."
            elif period >= 12 and period < 17:
                response = "Good afternoon, What help do you need from me."
            else:
                response = "Good Evening, How may i be of help"
        else:
            response = generate_response(user_query)
    else:
        response = "Hi, welcome to AidBot! What can i help you with?"

    return render(request, "chatbot.html", {"response": response})


def get_response(request):
    if request.method == 'GET':
        user_query = request.GET.get("msg")
        if user_query in greeting_queries:
            if period >= 0 and period < 12:
                response = "Good morning, I'm always here to help you."
            elif period >= 12 and period < 17:
                response = "Good afternoon, What help do you need from me."
            else:
                response = "Good Evening, How may i be of help"
        else:
            response = generate_response(user_query)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)