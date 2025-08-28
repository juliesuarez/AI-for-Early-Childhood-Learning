import os
import stripe
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template, session, redirect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Configure the Gemini API
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    print("Gemini API configured successfully!")
except AttributeError:
    print("Error: Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")
    model = None

YOUR_DOMAIN = 'http://127.0.0.1:5000'

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

    # Initialize session for new users
    if 'free_uses' not in session:
        session['free_uses'] = 2
        session['credits'] = 0

    # Check if the user has any uses left
    if session['free_uses'] > 0:
        session['free_uses'] -= 1
    elif session.get('credits', 0) > 0:
        session['credits'] -= 1
    else:
        # No free uses or credits left, ask for payment
        return jsonify({"action": "payment_required"})
    
    session.modified = True # Save the session changes

    # Get data from the frontend request
    data = request.json
    age_range = data.get('age_range')
    topic = data.get('topic')

    if not age_range or not topic:
        return jsonify({"error": "Age range and topic are required"}), 400

    # This is our prompt to the AI.
    prompt = f"""
    You are an expert in early childhood education.
    Provide a simple, positive, and actionable learning module for a parent.
    The child's age is {age_range}.
    The topic is {topic}.

    The response should be in two parts:
    1.  Learn: A short explanation (2-3 sentences).
    2.  Activity: A simple, fun activity (3-4 steps).

    Format the response as plain text, clearly labeling the 'Learn:' and 'Activity:' sections.
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({
            "module_text": response.text,
            "free_uses_left": session['free_uses'],
            "credits_left": session['credits']
        })
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({"error": "Failed to get a response from the AI."}), 500


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    """Creates a Stripe Checkout session and returns the redirect URL."""
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'ugx',
                        'product_data': {
                            'name': 'ParentPal AI Credit Pack',
                        },
                        'unit_amount': 1500000, 
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/',
        )
        return jsonify({'url': checkout_session.url})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/success')
def success():
    """Handles successful payments by adding credits to the user's session."""
    session['credits'] = session.get('credits', 0) + 10 # Add 10 credits
    session['free_uses'] = 0 # Ensure free uses are depleted
    return redirect('/') # Redirect back to the main page

# This makes the app runnable
if __name__ == '__main__':
    app.run(debug=True)