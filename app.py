import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure the Gemini API
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    print("Gemini API configured successfully!")
except AttributeError:
    print("Error: Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
    model = None

# Route for the main page
@app.route('/')
def index():
    """Renders the main HTML page."""
    return render_template('index.html')

# API endpoint to get the learning module
@app.route('/get_module', methods=['POST'])
def get_module():
    """
    Receives child's age and topic, gets advice from Gemini, and returns it.
    """
    if not model:
        return jsonify({"error": "AI model not configured"}), 500

    # Get data from the frontend request
    data = request.json
    age_range = data.get('age_range')
    topic = data.get('topic')

    if not age_range or not topic:
        return jsonify({"error": "Age range and topic are required"}), 400

    # This is our prompt to the AI. We're telling it exactly what we want.
    prompt = f"""
    You are an expert in early childhood education.
    Provide a simple, positive, and actionable learning module for a parent.
    The child's age is {age_range}.
    The topic is {topic}.

    The response should be in two parts:
    1.  **Learn:** A short, easy-to-understand explanation (2-3 sentences) of why this topic is important for this age.
    2.  **Activity:** A simple, fun, and practical activity (3-4 steps) the parent can do with their child using common household items.

    Format the response as plain text, clearly labeling the 'Learn:' and 'Activity:' sections.
    """

    try:
        # Send the prompt to the Gemini model
        response = model.generate_content(prompt)
        
        # Return the AI's generated text in a JSON object
        return jsonify({"module_text": response.text})
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({"error": "Failed to get a response from the AI."}), 500

# This makes the app runnable
if __name__ == '__main__':
    app.run(debug=True)