# AI Text Analyzer - Streamlit Application
![Project Logo](cursor1.png)

## Overview
A powerful text analysis web application built with Streamlit and Python, featuring AI-powered text processing capabilities using Cursor.ai integration.

## Live Demo
[http://localhost:8501]

## Project Structure
```plaintext
DEMOAPPCursor/
├── backend/
│   ├── app.py          # Streamlit application
│   ├── main.py         # Core logic and AI processing
│   └── requirements.txt # Python dependencies
├── cursor1.png         # Project logo/screenshot
├── .gitignore         # Git ignore rules
└── package-lock.json  # Node.js dependencies lock file
```

## Features
- 🤖 AI-Powered Text Analysis
- 📊 Interactive Data Visualization
- 🎨 Modern Streamlit UI
- ⚡ Real-time Processing
- 📱 Responsive Design

## Prerequisites
- Python 3.8+
- Streamlit
- Git

## Installation

1. Clone the repository
```bash
git clone https://github.com/Manobhiramlol/AI-Text-Analyser-Cursor.ai.git
cd AI-Text-Analyser-Cursor.ai
```

2. Set up Python virtual environment
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app locally:
```bash
cd backend
streamlit run app.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## Deployment
### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy the app

### Deploy using Docker
```bash
# Build the Docker image
docker build -t ai-text-analyzer .

# Run the container
docker run -p 8501:8501 ai-text-analyzer
```

## Development
### Adding New Features
1. Create a new branch:
```bash
git checkout -b feature/new-feature
```

2. Implement your changes
3. Test locally using:
```bash
streamlit run app.py
```

4. Create a pull request

### Local Development
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8
```

## Streamlit Components Used
- `st.title()` - Main application title
- `st.text_area()` - Text input
- `st.button()` - Action buttons
- `st.markdown()` - Rich text display
- [Add other Streamlit components you've used]

## Screenshots
![Application Screenshot](cursor1.png)

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Common Issues & Solutions
1. **Streamlit Cache Issues**
   - Clear cache: `streamlit cache clear`
   - Restart the Streamlit server

2. **Package Conflicts**
   - Update requirements: `pip freeze > requirements.txt`
   - Clean install: `pip install -r requirements.txt --clean`

## Performance Tips
- Use `@st.cache_data` for data loading
- Implement pagination for large datasets
- Optimize image sizes
- Use async operations for heavy processing

## Contact
- Developer: [@Manobhiramlol](https://github.com/Manobhiramlol)
- Project Link: https://github.com/Manobhiramlol/AI-Text-Analyser-Cursor.ai

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the amazing framework
- Cursor.ai for AI capabilities
- All contributors and testers
- This is An Internship Contributions (POC) @ Blackcoffer
---
Last updated: 2025-06-11 14:58:12 UTC
