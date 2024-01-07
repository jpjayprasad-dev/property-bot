# Project Report: Real Estate Chatbot

## Objectives:

The primary objectives of the Real Estate Chatbot project are:

1. **Development of an AI Real Estate Agent:**
   - Implement a chatbot capable of answering queries related to real estate properties.
   - Enable users to inquire about property details, prices, and other relevant information.

2. **Embedding Generation and Storage:**
   - Develop a script (store.py) to generate embeddings for real estate property web pages.
   - Store the generated embeddings locally for future retrieval and use in chat interactions.

3. **User Interaction through Chatbot:**
   - Implement a chat interface (chat.py) for users to interact with the AI real estate agent.
   - Provide a seamless experience for users to inquire about specific properties.

## Design:

### Overall System Design:

The Real Estate Chatbot system comprises three main components:

1. **Embedding Generation (store.py):**
   - Takes property name and URL as inputs.
   - Utilizes OpenAI API and Apify for web page content extraction and embedding generation.
   - Stores generated embeddings locally for future use.

2. **Chatbot (chat.py):**
   - Accepts the property name as input.
   - Uses the OpenAI GPT-3.5-turbo model to generate responses.
   - Facilitates a conversation-like interaction with users.

3. **Common Components:**
   - **OpenAI Integration:** Utilizes the OpenAI API for both embedding generation and chatbot responses.
   - **Apify Integration:** Employs Apify for web page content extraction during embedding generation.

### Layered Architecture:

The project follows a layered architecture:

1. **Data Layer:**
   - Storage of property embeddings.
   - Local storage is used for simplicity, but a database integration could be considered for scalability.

2. **Logic Layer:**
   - Embedding Generation Logic: Logic for interacting with OpenAI and Apify for embedding generation.
   - Chatbot Logic: Implementation of the chatbot using the OpenAI GPT-3.5-turbo model.

3. **Presentation Layer:**
   - Command-line interface for user interaction.
   - Output presentation for chat interactions.

## Implementation:

### Embedding Generation (store.py):

- Utilizes OpenAIEmbedding and Apify for embedding generation.
- Command-line script with options for property name and URL.
- Generates embeddings and stores them as JSON files locally.

### Chatbot (chat.py):

- Uses LLMPredictor with the OpenAI GPT-3.5-turbo model.
- Command-line script with an option for property name.
- Facilitates a chat-like interaction by sending user prompts and receiving AI-generated responses.

### Common Components:

- **OpenAI Integration:**
  - Integrated through the llama_index.llms.OpenAI module.
  - Customizable settings such as temperature, max_tokens, etc.

- **Apify Integration:**
  - Utilizes Apify for web page content extraction during embedding generation.

## Challenges:

1. **API Integration:**
   - Integrating and configuring both the OpenAI API and Apify required thorough understanding and careful parameter tuning.

2. **User Experience:**
   - Designing a user-friendly chat interaction while considering various user inputs and expectations.

3. **Embedding Storage:**
   - Deciding on an efficient and scalable strategy for storing property embeddings.

## Lessons Learned:

1. **API Usage and Rate Limiting:**
   - Gained experience in utilizing external APIs and managing rate limits to prevent service disruptions.

2. **User Interface Design:**
   - Learned the importance of intuitive design for user interactions and feedback.

3. **Embedding Strategies:**
   - Explored different strategies for generating and storing embeddings, considering both accuracy and efficiency.

## Conclusion:

The Real Estate Chatbot project successfully achieved its objectives of creating an AI real estate agent capable of handling user queries through a chat interface. The system design ensures flexibility for future enhancements, and the implementation demonstrates integration with external APIs and tools.

## Future Enhancements:

1. **Database Integration:**
   - Implement a database for storing property embeddings, allowing for better scalability.

2. **Enhanced Chat Experience:**
   - Implement more sophisticated chat features, such as multi-turn conversations and context-aware responses.

3. **Web Interface:**
   - Develop a web-based interface for a more accessible user experience.
