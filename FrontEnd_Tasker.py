import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the task data
tasks = pd.read_csv("tasks.csv")

# Create a TF-IDF vectorizer to convert task descriptions into vectors
vectorizer = TfidfVectorizer(stop_words="english")

# Fit the vectorizer to the task descriptions and transform them into vectors
task_vectors = vectorizer.fit_transform(tasks["description"])

# Create a cosine similarity matrix from the task vectors
similarity_matrix = cosine_similarity(task_vectors)

# Load the pre-trained LLMs model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("llm-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("llm-base-uncased")

# Define a function to generate a task plan based on the user's input
def generate_task_plan(user_input):
    # Tokenize the user's input
    input_tokens = tokenizer.encode(user_input, return_tensors="pt")

    # Get the top 5 most similar tasks to the user's input
    similar_tasks = np.argsort(-similarity_matrix[input_tokens])[:5]

    # Generate a task plan based on the similar tasks
    task_plan = []
    for task_id in similar_tasks:
        task = tasks.iloc[task_id]
        task_plan.append({"task_id": task_id, "task_name": task["name"], "task_description": task["description"]})

    return task_plan

# Define a function to update the task plan based on the user's feedback
def update_task_plan(task_plan, user_feedback):
    # Tokenize the user's feedback
    feedback_tokens = tokenizer.encode(user_feedback, return_tensors="pt")

    # Get the top 5 most similar tasks to the user's feedback
    similar_tasks = np.argsort(-similarity_matrix[feedback_tokens])[:5]

    # Update the task plan based on the similar tasks
    updated_task_plan = []
    for task_id in similar_tasks:
        task = tasks.iloc[task_id]
        updated_task_plan.append({"task_id": task_id, "task_name": task["name"], "task_description": task["description"]})

    return updated_task_plan

# Create a front-end task manager and planner
class TaskManager:
    def __init__(self):
        self.task_plan = []

    def generate_task_plan(self, user_input):
        self.task_plan = generate_task_plan(user_input)
        return self.task_plan

    def update_task_plan(self, user_feedback):
        self.task_plan = update_task_plan(self.task_plan, user_feedback)
        return self.task_plan

# Create an instance of the task manager and planner
task_manager = TaskManager()

# Test the task manager and planner
user_input = "I need to plan a trip to Europe"
task_plan = task_manager.generate_task_plan(user_input)
print("Task Plan:", task_plan)

user_feedback = "I want to visit Paris and Rome"
updated_task_plan = task_manager.update_task_plan(user_feedback)
print("Updated Task Plan:", updated_task_plan)
