from agno.embedder.cohere import CohereEmbedder
from agno.vectordb.pineconedb import PineconeDb
from agno.knowledge.arxiv import ArxivKnowledgeBase
from app.config import COHERE_API_KEY, PINECONE_API_KEY, PINECONE_INDEX_NAME

embedder = CohereEmbedder(
    dimensions=1024,
    api_key=COHERE_API_KEY,
)

vector_db = PineconeDb(
    name=PINECONE_INDEX_NAME,
    dimension=1024,
    metric="cosine",
    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
    api_key=PINECONE_API_KEY,
    embedder=embedder,
)

def knowledge_base(topic: str):
    """Dynamically create & load Wikipedia + Arxiv KBs for a given topic into Pinecone."""
    knowledge = ArxivKnowledgeBase(queries=[topic], vector_db=vector_db, num_documents=20)
    
    knowledge.load(recreate=False,upsert=True)

    return knowledge