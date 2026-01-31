import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# 🔧 Load LLM
model = OllamaLLM(model="llama3.2")

# 🧠 Prompt Template
template = """
You are a friendly pizza expert assistant named PizzaBot 🍕. 
Answer questions using the following customer reviews. 
Be honest, helpful, and add a touch of personality. 
If the reviews don't contain enough info, it's okay to guess based on common themes.

Reviews:
{reviews}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# 🎨 Page Config
st.set_page_config(page_title="PizzaBot", page_icon="🍕", layout="centered")
st.title("🍕 PizzaBot")
st.markdown("_Ask me anything about our restaurant's reviews!_")

# 📌 Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    PizzaBot is powered by local LLMs and real customer reviews.
    Built with **LangChain**, **Ollama**, and **Streamlit**.
    """)

# 💬 Session-based chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🕒 Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🧾 Get user input
user_input = st.chat_input("Ask your question about the restaurant...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔍 Retrieve relevant reviews
    retrieved_docs = retriever.invoke(user_input)
    formatted_reviews = "\n".join([f"- {doc.page_content}" for doc in retrieved_docs])

    # 📂 Show retrieved reviews
    with st.expander("🔍 Reviews used"):
        st.markdown(formatted_reviews)

    # 🤖 Generate response
    response = chain.invoke({
        "reviews": formatted_reviews,
        "question": user_input
    })

    # Save and show assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(f"✅ **PizzaBot:**\n\n{response}")

        # Optional: Show JSON (for dev/debug/future integration)
        st.json({
            "question": user_input,
            "answer": response,
            "top_reviews": [doc.page_content for doc in retrieved_docs]
        })

# 📌 Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, LangChain, and Ollama")
