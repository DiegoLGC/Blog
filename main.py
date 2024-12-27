import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="Blog Post Generator")
st.title("Blog Post Generator")

# Entrada de la clave API
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if not openai_api_key or not openai_api_key.startswith("sk-"):
    st.warning("Enter a valid OpenAI API Key")
    st.stop()

# Entrada del tema
topic_text = st.text_input("Enter topic: ")

if not topic_text.strip():
    st.warning("Please enter a topic for the blog post.")
    st.stop()

if len(topic_text) > 100:
    st.warning("The topic is too long. Please use fewer than 100 characters.")
    st.stop()

# Generar respuesta
def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    As an experienced startup and venture capital writer, 
    generate a 400-word blog post about {topic}.
    """
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )
    query = prompt.format(topic=topic)
    response = llm.generate([query])
    blog_post = response.generations[0][0].text  # Ajusta según el formato de respuesta
    word_count = len(blog_post.split())
    
    st.write(blog_post)
    st.write(f"This post has {word_count} words.")

generate_response(topic_text)

        
