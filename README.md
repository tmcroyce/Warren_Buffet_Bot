# README: Warren Buffet Bot

## Overview
Warren Buffet Bot is an AI-powered application that answers user questions in the style of Warren Buffet. 
The application uses OpenAI's GPT model, Pinecone vector store, and Langchain's library to provide accurate responses based on similarity search and question-answering techniques.

To try out a LIVE version of the model, check here: [Warren Buffet Bot](https://tmcroyce-warren-buffet-bot-warren-buffet-bot-s69fyw.streamlit.app/)

## Dependencies
- langchain
- openai
- pinecone
- streamlit

## How to use
1. Ensure you have all the required dependencies installed.
2. Replace the `st.secrets` values with your own API keys for OpenAI and Pinecone.
3. Run the application using Streamlit: `streamlit run <filename.py>`
4. Open the provided URL in your browser.
5. Enter a question for Warren Buffet in the input field and press "Go".
6. The bot will return an answer based on the most relevant source documents.

## Application Structure
- The application uses OpenAI Embeddings to convert text queries into vector space.
- Pinecone is initialized with the provided API key and environment details.
- A Pinecone Index is created to store and search the vectorized documents.
- The Langchain library is utilized to load a question-answering chain and execute it.
- Streamlit is used for the web application interface, displaying input fields, buttons, and answers.

## Application Components
- `OpenAIEmbeddings`: Converts text strings into vector space using OpenAI API.
- `Pinecone`: A vector store that enables efficient similarity search on embeddings.
- `OpenAI`: A low-level language model (LLM) leveraging GPT for generating answers.
- `load_qa_chain`: Loads a question-answering chain for generating answers.
- `vectorstore`: A Pinecone instance for storing and searching document vectors.
- `chain`: An instance of the question-answering chain for generating answers.

## Customization
- Modify the HTML and CSS in the `st.markdown` sections to change the appearance of the application.
- Adjust the number of documents returned in the similarity search by changing the `top_k` parameter in the `vectorstore.similarity_search()` method.
- Customize the temperature parameter for the `OpenAI` instance to control the randomness of the generated answers.
