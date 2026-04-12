import json
from llm import generate_response
from rag import get_context
from tools import mock_lead_capture

# Optional (for requirement mention)


class Agent:
    def __init__(self):
        self.state = {
            "stage": "chat",   # chat / collecting
            "intent": None,
            "name": None,
            "email": None,
            "platform": None
        }

    def respond(self, user_input):

        # If collecting lead info → structured flow
        if self.state["stage"] == "collecting":
            return self.handle_lead_collection(user_input)

        context = get_context()

        # 🔥 LLM does BOTH: intent detection + response
        prompt = f"""
You are an AI sales assistant for AutoStream.

Your tasks:
1. Classify intent into:
   - greeting
   - pricing
   - high_intent
   - general

2. Answer naturally using knowledge base.

Knowledge Base:
{context}

Rules:
- If pricing question → explain clearly
- If high intent → say: "Let's get you started."
- Keep response short and natural

User: {user_input}

Return ONLY JSON:
{{
  "intent": "...",
  "response": "..."
}}
"""

        llm_output = generate_response(prompt)

        # 🔥 Parse JSON safely
        try:
            parsed = json.loads(llm_output)
            intent = parsed.get("intent", "general")
            response = parsed.get("response", "")

        except:
            intent = "general"
            response = llm_output  # fallback

        self.state["intent"] = intent

        # 🔥 Trigger lead flow ONLY if high intent
        if intent == "high_intent":
            self.state["stage"] = "collecting"
            return response + "\n\nWhat's your name?"

        return response

    def handle_lead_collection(self, user_input):

        if not self.state["name"]:
            self.state["name"] = user_input
            return "Nice to meet you! 😊 What's your email?"

        elif not self.state["email"]:
            self.state["email"] = user_input
            return "Great! Which platform do you create content on?"

        elif not self.state["platform"]:
            self.state["platform"] = user_input

            # ✅ Call tool ONLY after all inputs
            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"]
            )

            # Reset state
            self.state = {
                "stage": "chat",
                "intent": None,
                "name": None,
                "email": None,
                "platform": None
            }

            return "🎉 You're all set! We'll contact you soon."

        return "Something went wrong."
