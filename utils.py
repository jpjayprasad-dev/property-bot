import json
import os
from llama_index.readers.schema import Document
from llama_index import PromptHelper, OpenAIEmbedding
#from llama_index.embeddings import LangchainEmbedding
from llama_index.llms import OpenAI
from llama_index.text_splitter import TokenTextSplitter
#from langchain.embeddings.huggingface import HuggingFaceEmbeddings

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_KEY') if os.getenv('OPENAI_KEY') else open("OPEN_AI_KEY.txt", "r").read().strip("\n")

# Converts a single record from the Actor's resulting dataset to the LlamaIndex format
def tranform_dataset_item(item):
    print(item)
    return Document(
        text=item.get("text"),
        extra_info={
            "url": item.get("url"),
        },
    )


def load_docs_from_json(out_path, url=""):
    with open(out_path, 'r') as file:
        documents = json.load(file)

    if url:
        documents=[doc for doc in documents if doc.get("url") == url]

    return documents

# Convert LlamaIndex Documents to JSON format
def dump_docs_to_json(documents, out_path):
    """Convert LlamaIndex Documents to JSON format and save it."""
    result_json = load_docs_from_json(out_path)
    for doc in documents:
        cur_dict = {
            "text": doc.get_text(),
            "id": doc.get_doc_id(),
            "url": doc.extra_info["url"],
        }
        result_json.append(cur_dict)
    json.dump(result_json, open(out_path, 'w'))

 # Initialize an LLMPredictor object with a specific OpenAI model and settings
llm = OpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=256)

# load in HF embedding model from langchain
# embed_model = LangchainEmbedding(HuggingFaceEmbeddings())

# Initialize an OpenAIEmbedding model
embed_model = OpenAIEmbedding()

# Initialize a TokenTextSplitter with custom chunking settings
node_parser = TokenTextSplitter(chunk_size=2000, chunk_overlap=50)

# Initialize a PromptHelper with specific context and output settings
prompt_helper = PromptHelper(
    context_window=4096,
    num_output=512,
    chunk_overlap_ratio=0.1,
)