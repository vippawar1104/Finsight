from dotenv import load_dotenv
import os

load_dotenv()


def get_budget_insights(user_query, transactions_text):
    """Return a Cohere-generated budget insight or a helpful message if Cohere isn't available.
    This does a lazy import of the cohere package so importing this module won't crash the app when
    cohere is not installed.
    """
    try:
        import cohere
    except ModuleNotFoundError:
        return "FinBot is not available because the 'cohere' package is not installed. Install it with: pip install cohere"

    api_key = os.getenv('COHERE_API_KEY')
    if not api_key:
        return "FinBot is not configured: COHERE_API_KEY not found in the environment. Add it to a .env file."

    try:
        co = cohere.Client(api_key)

        system_message = '''You are FinBot, a financial AI assistant developed by Sakshi & Shahu for the Finsight Finance Tracker. Respond to the user in a single, well-structured paragraph, ensuring that all sentences are complete and coherent, without any breaks or cutoff.
Your job is ONLY to assist users with their financial queries, including budgeting, expense tracking, and savings advice. DO NOT answer anything that is unrelated to finance. If a user asks something outside finance, firmly respond with:
"I can only assist with financial-related questions. Please ask me something about your finances."
If user asks about making changes to his expenses or income to delete or add, simply respond:
"I can assist you with managing your finances, but I cannot make changes to your expenses or income. You can update or modify them on the respective pages. Let me know if you'd like help with anything else!"
If the user asks about yourself, simply respond:
"I am FinBot, a financial assistant built by Sakshi & Shahu to help with budgeting and expense management."'''

        user_message = f"User query: {user_query}\n\nTransactions data: {transactions_text}"

        response = co.chat(
            model='command-a-03-2025',
            preamble=system_message,
            message=user_message,
            max_tokens=200
        )

        return response.text.strip()

    except Exception as e:
        # Return a readable error message instead of raising so the Streamlit app remains up
        return f"FinBot error: {str(e)}"