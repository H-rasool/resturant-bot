# 🍕 PizzaBot - Local AI Restaurant Review Assistant

A Retrieval-Augmented Generation (RAG) application that answers questions about restaurant reviews using local LLMs. Built with LangChain, Ollama, ChromaDB, and Streamlit.

## 📋 Overview

PizzaBot is an AI-powered assistant that helps users query and understand restaurant reviews through natural language questions. The application uses:

- **Vector Database (ChromaDB)**: Stores and retrieves relevant restaurant reviews
- **Local LLM (Ollama)**: Generates answers using the `llama3.2` model
- **Embeddings (Ollama)**: Uses `mxbai-embed-large` for semantic search
- **Streamlit**: Provides an interactive web interface

The system retrieves the top 10 most relevant reviews based on your question and uses them as context for generating accurate, review-based answers.

## 🏗️ Project Structure

```
Local AI Agent/
├── app.py                          # Streamlit web application
├── main.py                         # Command-line interface
├── vector.py                       # Vector database setup and retriever
├── realistic_restaurant_reviews.csv  # Restaurant review dataset
├── chrome_langchain_db/            # ChromaDB persistent storage
├── requirements.txt                # Python dependencies
└── README.md                        # This file
```

## 🚀 Features

- **Dual Interface**: 
  - Web-based chat interface via Streamlit (`app.py`)
  - Command-line interface for terminal usage (`main.py`)
- **Semantic Search**: Retrieves relevant reviews using vector similarity
- **Local Processing**: All AI processing happens locally using Ollama
- **Persistent Storage**: Vector database persists between sessions
- **Review Context**: Shows which reviews were used to generate each answer

## 📦 Prerequisites

1. **Python 3.8+**
2. **Ollama** installed and running locally
   - Download from: https://ollama.ai/
   - Required models:
     - `llama3.2` (for LLM)
     - `mxbai-embed-large` (for embeddings)

### Installing Ollama Models

After installing Ollama, run these commands:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

## 🔧 Installation

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install streamlit  # Required for app.py but not in requirements.txt
   ```

## 🎯 Usage

### Web Interface (Streamlit)

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

**Features:**
- Interactive chat interface
- View retrieved reviews used for each answer
- Chat history maintained during session
- JSON output for debugging/integration

### Command-Line Interface

Run the CLI version:

```bash
python main.py
```

**Usage:**
- Type your question and press Enter
- Type `q` to quit
- Answers are generated based on retrieved reviews

## 🔍 How It Works

1. **Data Loading**: Restaurant reviews from `realistic_restaurant_reviews.csv` are loaded into a ChromaDB vector database
2. **Embedding**: Each review is converted to a vector using Ollama embeddings
3. **Query Processing**: When you ask a question:
   - Your question is embedded into a vector
   - Similar reviews are retrieved using vector similarity search (top 10)
   - Retrieved reviews are formatted and passed as context to the LLM
4. **Answer Generation**: The LLM generates an answer based on the retrieved review context

### Vector Database Initialization

The vector database is automatically created on first run. The `chrome_langchain_db/` directory stores the persistent vector embeddings. If you want to rebuild the database, delete this directory and restart the application.

## 📊 Data Format

The CSV file (`realistic_restaurant_reviews.csv`) contains restaurant reviews with the following columns:
- **Title**: Review title
- **Date**: Review date (YYYY-MM-DD)
- **Rating**: Rating (1-5)
- **Review**: Full review text

Each review is stored as a document with metadata (rating, date) in the vector database.

## 🛠️ Configuration

### Changing the LLM Model

Edit `app.py` or `main.py`:
```python
model = OllamaLLM(model="your-model-name")
```

### Changing the Embedding Model

Edit `vector.py`:
```python
embeddings = OllamaEmbeddings(model="your-embedding-model")
```

### Adjusting Number of Retrieved Reviews

Edit `vector.py`:
```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}  # Change 10 to desired number
)
```

## 📝 Dependencies

- `langchain`: Core LangChain framework
- `langchain-ollama`: Ollama integration for LangChain
- `langchain-chroma`: ChromaDB integration for LangChain
- `pandas`: Data manipulation for CSV processing
- `streamlit`: Web interface framework

## 🐛 Troubleshooting

### Ollama Connection Issues
- Ensure Ollama is running: `ollama list` should show your models
- Check if models are downloaded: `ollama pull llama3.2`

### Vector Database Issues
- If you encounter database errors, delete `chrome_langchain_db/` and restart
- Ensure you have write permissions in the project directory

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt streamlit`
- Verify your virtual environment is activated

## 🔮 Future Enhancements

Potential improvements:
- Add support for multiple restaurants/datasets
- Implement review filtering by rating or date
- Add export functionality for conversations
- Support for custom CSV files
- Multi-language support
- Enhanced UI with review visualization

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Support

For issues related to:
- **Ollama**: Visit https://github.com/ollama/ollama
- **LangChain**: Visit https://github.com/langchain-ai/langchain
- **Streamlit**: Visit https://github.com/streamlit/streamlit

---

Built with ❤️ using Streamlit, LangChain, and Ollama
