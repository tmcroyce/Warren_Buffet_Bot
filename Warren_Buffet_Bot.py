from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain
import pinecone
import os
import openai
import streamlit as st


# set page config
st.set_page_config(page_title='Warren Buffet Bot',
                    page_icon='images/warren.jpg',
                    initial_sidebar_state='auto',
                    # change color
                    layout='centered',
                    menu_items={ 'Get Help': 'https://www.travisroyce.com/',
                                'Report a bug': "mailto:traviscroyce@gmail.com",
                                    'About': "https://www.travisroyce.com/"
})

# Set dark theme

# OpenAI API key
openai.api_key =st.secrets['openAI_API_Key']

#Embeddings - turning string to vector space
embeddings = OpenAIEmbeddings(openai_api_key=st.secrets['openAI_API_Key'])

#init Pinecone
pinecone.init(
    api_key = st.secrets['pinecone_api_key'],
    environment = st.secrets['pinecone_api_environment']
)
index_name = 'langchain1'
index = pinecone.Index("langchain1")

# Load Vectorstore
vectorstore = Pinecone(index, embeddings.embed_query, "text")

llm = OpenAI(temperature=0, openai_api_key=st.secrets['openAI_API_Key'])
chain = load_qa_chain(llm, chain_type='stuff')

st.markdown("""
    <style>
    .custom-title {
        text-align: center;
        color: white;
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #142630 30%, #030a14 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 0 auto;
        width: 100%;
        box-shadow: 0 4p   x 6px rgba(0, 0, 0, 0.1), 0 2px 4px rgba(0, 0, 0, 0.06);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="custom-title">What Would Warren Do?</div>', unsafe_allow_html=True)

st.write(' ')
st.write(' ')
st.write(' ')

# load image in sidebar
st.sidebar.image('images/warren2.png', width=300, caption= 'Robot Warren Buffet courtesy of midjourney AI')

os.environ['OPENAI_API_KEY'] = st.secrets['openAI_API_Key']

# markdown title with coloring
# st.write('Welcome to Warren Buffet Bot')
# st.write('Ask Warren Buffet a question and he will answer it')

#Ask Warren Buffet a question
query = st.text_input('Ask Warren Buffet a question and press GO!',)



# prompt weither to show source documents
#show_source = st.checkbox('Show source documents')

# add go button
go = st.button('Go')

if go:
    docs = vectorstore.similarity_search(query, include_metadata=True, top_k=3)
    answer = chain.run(input_documents= docs, question = query)
    st.write('Robot Warren Buffet Answers:', answer)

