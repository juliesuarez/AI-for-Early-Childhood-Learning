# ParentPal AI 🤖

ParentPal AI is a web application designed to solve SDG's. It serves as an AI-powered assistant for parents, providing simple, actionable advice and learning modules on early childhood education.

# The Core Feature

A parent can select their child's age and a topic of interest (e.g., "Language Development"). The application then leverages a generative AI to provide a concise learning tip and a fun, practical activity the parent can do with their child.

# Tech Stack

# Backend: Python with the Flask micro-framework.
# AI: Google's Gemini API (`gemini-1.5-flash-latest`).
# Frontend: HTML, CSS, and vanilla JavaScript.
# Deployment:Render (PaaS).

# Setup and Installation

To run this project locally, follow these steps:

1.  Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/parentpal-ai.git](https://github.com/your-username/parentpal-ai.git)
    cd parentpal-ai
    ```

2.  Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  set up your environment variables:**
    # Create a file named `.env` in the root directory.
    # Add your Gemini API key to this file:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

4.  Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.