import argparse
import os
from llama_index import load_index_from_storage, ServiceContext, StorageContext
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import OpenAIAgent, OpenAIAssistantAgent

from utils import llm, embed_model, node_parser, prompt_helper

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_KEY') if os.getenv('OPENAI_KEY') else open("OPEN_AI_KEY.txt", "r").read().strip("\n")

def initialize_chat(property_name):
    # Create a ServiceContext by combining the above components
    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        node_parser=node_parser,
        prompt_helper=prompt_helper
    )

    storage_context = StorageContext.from_defaults(
            persist_dir=f"./storage/{property_name}"
    )

    index = load_index_from_storage(
        storage_context, service_context=service_context
    )

    # Initialize a query engine for the index with a specified similarity top-k value
    query_engine = index.as_query_engine(similarity_top_k=3)

    individual_query_engine_tools = [QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name=f"vector_index_property_{property_name}",
                description=f"useful for when you want to answer queries about the real estate property {property_name}",
            ),
        )]

    tools = individual_query_engine_tools

    """
    agent = OpenAIAssistantAgent.from_new(
        name="Property bot",
        instructions="You are a bot designed to answer questions about the real estate property. \
                        Start the conversation with greeting the user 'Sawadee Ka'. \
                        Ask the name of the user at the beginning of the chat. \
                        Ignore the data from 'Recommended Units' while answering the questions",
        tools=tools,
        instructions_prefix="Please address the user with a prefix Khun. The user name has to be collected at the begninning of the chat",
        verbose=True,
    )
    """


    agent = OpenAIAgent.from_tools(
        system_prompt=f"""
        You are an AI real estate agent designed to answer queries about the real estate property {property_name}.
        Start the conversation with greeting the user 'Sawadee Ka'. Ask the name of the user at the beginning of the chat.
        Please address the user with a prefix Khun on further conversation.
        Please always use the tools provided to answer a question. Do not rely on prior knowledge.
        Ignore the listings provided under 'Recommended Units' from the tools while answering the questions".
        The selling price of the property will be provided in the format "Buy : <price>" in the data from the tools.
        Refer this example of how price is mentioned in the tools eg: "Buy : \u0e3f6,099,000"
        """,
        llm=llm,
        tools=tools, 
        verbose=False        
    )

    user_query = ""

    while user_query != 'exit':
        user_query = input("Ask a question: ")
        response = agent.chat(user_query)
        print(str(response))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Embed and store property data.")
    parser.add_argument("property_name", help="property name")

    args = parser.parse_args()

    property_name = args.property_name

    initialize_chat(property_name)

