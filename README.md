# ParentPal AI 🤖

ParentPal AI is a web application designed to solve SDG's. It serves as an AI-powered assistant for parents, providing simple, actionable advice and learning modules on early childhood education.

# The Core Feature

A parent can select their child's age and a topic of interest (e.g., "Language Development"). The application then leverages a generative AI to provide a concise learning tip and a fun, practical activity the parent can do with their child.

# Tech Stack

# Backend: Python with the Flask micro-framework.
# AI: Google's Gemini API (`gemini-1.5-flash-latest`).
# Payments:Stripe API for handling credit pack purchases.
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
    SECRET_KEY="A_STRONG_RANDOM_STRING_FOR_SESSIONS"
    STRIPE_SECRET_KEY="sk_test_YOUR_STRIPE_SECRET_KEY_HERE"
    ```

4.  Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

5. Deploy on Render
# Go to render.com and sign up with your GitHub account.
On your dashboard, click New + and select Web Service.
Connect the GitHub repository you just created (parentpal-ai).
Fill out the deployment settings:
Name: parentpal-ai (or any name you like).
Region: Choose one (e.g., Frankfurt).
Runtime: Python 3.
Build Command: pip install -r requirements.txt. (Render usually auto-detects this).
Start Command: This is important! Use the Gunicorn command: gunicorn app:app.
Scroll down to Environment Variables.
Click Add Environment Variable.
For the key, enter GEMINI_API_KEY.
For the value, paste your actual API key.
Click Create Web Service.
# Once it's done, you'll have a public URL for your live project

# Prompt Used: Education: Provides AI-guided learning modules for parents on early childhood education
# AI Used: Gemini

Built with ❤️ by:
Name: Juliet Nakawesi from Uganda
Role: Software Developer

Name: Stacy Njoga from Kenya
Role: Business developer