import streamlit as st
from transformers import pipeline
import json
import textwrap

# Initialize the models (will download on first run)
@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return summarizer, sentiment_analyzer

# Configure Streamlit page
st.set_page_config(
    page_title="AI Text Analyzer",
    page_icon="📝",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        height: 200px;
    }
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

def chunk_text(text, max_chunk_size=500):
    # Split text into sentences
    sentences = text.replace('\n', ' ').split('.')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for sentence in sentences:
        sentence = sentence.strip() + '.'
        sentence_size = len(sentence.split())
        
        if current_size + sentence_size > max_chunk_size:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_size = sentence_size
        else:
            current_chunk.append(sentence)
            current_size += sentence_size
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def extract_key_points(text, max_points=5):
    # Simple key points extraction based on sentences
    sentences = text.split('.')
    # Filter out empty or very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    # Return up to max_points sentences as key points
    return sentences[:max_points]

def analyze_text(text: str):
    try:
        # Load models
        summarizer, sentiment_analyzer = load_models()

        # Calculate basic metrics
        word_count = len(text.split())
        reading_time_mins = max(1, round(word_count / 200))  # Assuming 200 words per minute
        reading_time = f"{reading_time_mins} min{'s' if reading_time_mins > 1 else ''}"

        # Split text into chunks for processing
        chunks = chunk_text(text)
        
        # Generate summary from first chunk (or combine summaries if needed)
        summary = summarizer(chunks[0], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        
        # Analyze sentiment of each chunk and average the results
        sentiments = []
        for chunk in chunks:
            chunk_sentiment = sentiment_analyzer(chunk)[0]
            sentiments.append((chunk_sentiment['label'], chunk_sentiment['score']))
        
        # Determine overall sentiment
        positive_count = sum(1 for label, _ in sentiments if label == 'POSITIVE')
        total_count = len(sentiments)
        avg_score = sum(score for _, score in sentiments) / total_count
        
        overall_sentiment = 'POSITIVE' if positive_count > total_count/2 else 'NEGATIVE'
        sentiment = f"{overall_sentiment} ({round(avg_score * 100)}% confidence)"

        # Extract key points from the entire text
        key_points = extract_key_points(text)

        return {
            "summary": summary,
            "sentiment": sentiment,
            "key_points": key_points,
            "word_count": word_count,
            "reading_time": reading_time
        }
    except Exception as e:
        st.error(f"Error analyzing text: {str(e)}")
        return None

# Main app
st.title("📝 AI Text Analyzer")
st.markdown("""
Enter your text below to get an AI-powered analysis including summary, sentiment, and key points.
This version uses free, open-source models from Hugging Face! 🤗
""")

# Text input
text = st.text_area("Enter your text here", height=200)

# Analyze button
if st.button("Analyze Text", type="primary"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing your text... (First run may take a minute to download models)"):
            analysis = analyze_text(text)
            
            if analysis:
                # Create two columns for the results
                col1, col2 = st.columns(2)
                
                with col1:
                    # Summary
                    st.subheader("Summary")
                    st.write(analysis["summary"])
                    
                    # Sentiment
                    st.subheader("Sentiment Analysis")
                    sentiment = analysis["sentiment"]
                    st.write(sentiment)
                
                with col2:
                    # Key Points
                    st.subheader("Key Points")
                    for point in analysis["key_points"]:
                        st.markdown(f"• {point}")
                
                # Statistics in a nice format
                st.subheader("Statistics")
                stats_col1, stats_col2 = st.columns(2)
                with stats_col1:
                    st.metric("Word Count", analysis["word_count"])
                with stats_col2:
                    st.metric("Reading Time", analysis["reading_time"]) 