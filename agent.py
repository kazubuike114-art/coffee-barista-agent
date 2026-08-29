import json
from google.adk.agents import LlmAgent

def get_menu() -> str:
    """Retrieves the coffee shop menu from menu.json."""
    try:
        with open("menu.json", "r") as f:
            return f.read()
    except Exception as e:
        return json.dumps({"error": str(e)})

root_agent = LlmAgent(
    name="coffee_barista",
    model="gemini-2.5-flash",
    instruction="""You are a friendly and helpful AI Barista for a coffee shop. 
Your job is to help customers choose items from the menu, answer questions about ingredients, and take orders.
Rules you MUST follow:
* You must recommend items ONLY from the menu returned by get_menu().
* Do NOT recommend or suggest any item that is not present in the menu.
* If a user's preference is vague or unclear, ask exactly ONE friendly clarifying question to narrow down what they want.
* Be warm and welcoming, but remain professional.""",
    tools=[get_menu]
)
