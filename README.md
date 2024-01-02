# Real Estate Chatbot

This project implements a chatbot that serves as an AI real estate agent. The chatbot can answer queries about various real estate properties.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jpjayprasad-dev/property-bot
   cd property-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up OpenAI API Key and Apify Token:

   - Obtain an OpenAI API key from [OpenAI](https://beta.openai.com/signup/).
   - Set the API key as an environment variable:

     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```

   - Obtain an Apify token from [Apify](https://apify.com/).
   - Set the Apify token as an environment variable:

     ```bash
     export APIFY_TOKEN=your_apify_token
     ```

   Alternatively, create a file named "OPEN_AI_KEY.txt" for the OpenAI API key and create a file named "APIFY_TOKEN.txt" for the APIFY TOKEN.

## Usage

### Storing Property Embeddings

Run the following command to store property embeddings:

```bash
python store.py "Property Name" "https://property-url.com"
```

### Chatting with the AI Property Agent

Run the following command to start chatting with the AI property agent:

```bash
python chat.py "Property Name"
```

Note: Make sure to replace "Property Name" and "https://property-url.com" with the actual property details.

## Configuration

- **store.py**: Takes the real estate property name and the URL of the webpage where the property is listed as command-line arguments to generate embeddings of the webpage and store them locally.

- **chat.py**: Hosts an AI property agent chatbot. Takes the name of the property as a command-line argument, allowing users to check details of the property.
