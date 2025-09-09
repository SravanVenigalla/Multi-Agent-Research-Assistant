import os
from dotenv import load_dotenv

# Load API keys and environment variables
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX_NAME = os.getenv('PINECONE_INDEX_NAME', 'documents')