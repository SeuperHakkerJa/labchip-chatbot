import fire 
import openai
from dataclasses import dataclass
import dotenv
import os


from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
)

# find api key from local .env file
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')
if api_key is None:
    raise ValueError("API_KEY not found. Ensure your .env file has been configured correctly.")
openai.api_key = api_key

@dataclass
class RAG_Config():
    storage_path: str = './storage'
    query: str = 'tell me about labchip'
    rag_mode: str = 'tree_summarize'
        
        
def retrieve(cfg=RAG_Config()):
        
    storage_context = StorageContext.from_defaults(persist_dir=cfg.storage_path)
    index = load_index_from_storage(storage_context, index_id="vector_index")
    query_engine = index.as_query_engine(response_mode=cfg.rag_mode)
    response = query_engine.query(cfg.query)
        
    return response

def query(msg=''):
    cfg = RAG_Config()
    cfg.query = msg
    response = retrieve(cfg)

    return response.response

# def main(**kwargs):
#     cfg = RAG_Config(**kwargs)
#     response = retrieve(cfg)
#     print(response)  # Or however you want to handle the response


# if __name__ == '__main__':
#     fire.Fire(main)
    
