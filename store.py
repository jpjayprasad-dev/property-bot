import argparse
import json
import os

import nest_asyncio
from llama_index import download_loader, VectorStoreIndex, ServiceContext, StorageContext
from utils import tranform_dataset_item, llm, embed_model, node_parser, prompt_helper, dump_docs_to_json, load_docs_from_json


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_KEY') if os.getenv('OPENAI_KEY') else open("OPEN_AI_KEY.txt", "r").read().strip("\n")
APIFY_TOKEN = os.getenv('APIFY_TOKEN') if os.getenv('APIFY_TOKEN') else open("APIFY_TOKEN.txt", "r").read().strip("\n")

nest_asyncio.apply()

import logging
import sys

# Set up the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set logger level to INFO

# Clear out any existing handlers
logger.handlers = []

# Set up the StreamHandler to output to sys.stdout (Colab's output)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)  # Set handler level to INFO

# Add the handler to the logger
logger.addHandler(handler)

def embed_data(property_name, url):

    documents = load_docs_from_json('./storage/documents.json', url)
    if documents:
        documents = [tranform_dataset_item(doc) for doc in documents]
    else:
        ApifyActor = download_loader("ApifyActor")
        reader = ApifyActor(APIFY_TOKEN)

        documents = reader.load_data(
            actor_id="apify/website-content-crawler",
            run_input={"startUrls": [{"url": url}],},
            dataset_mapping_function=tranform_dataset_item,
        )
        
        """
        documents = reader.load_data(
            actor_id="apify/web-scraper",
            run_input={"startUrls": [{"url": url}],
            "pageFunction": '''
                async function pageFunction(context) {
                    const { request, log, jQuery } = context;
                    const url = window.location.href;
                    const text = jQuery('body').text();

                    // Extract data from the page
                    const title = jQuery('title').text();
                    log.info(`Title: ${title}`);

                    // Return the extracted data
                    return {
                        title: title,
                        url:url,
                        text:text
                    };
                }
            ''',
            },
            dataset_mapping_function=tranform_dataset_item,
        )
        """

        # Save the documents to a JSON file
        dump_docs_to_json(documents,'./storage/documents.json')

    print(documents)

    # Create a ServiceContext by combining the above components
    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        node_parser=node_parser,
        prompt_helper=prompt_helper
    )

    storage_context = StorageContext.from_defaults()

    # Create a VectorStoreIndex from a list of documents using the service context
    index = VectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)

    storage_context.persist(persist_dir=f"./storage/{property_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Embed and store property data.")
    parser.add_argument("property_name", help="property name")
    parser.add_argument("url", help="url to the property page")

    args = parser.parse_args()

    property_name = args.property_name
    url = args.url

    embed_data(property_name, url)