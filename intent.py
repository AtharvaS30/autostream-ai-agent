def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in user_input for word in ["price", "cost", "plan", "pricing"]):
        return "pricing"

    if any(word in user_input for word in ["buy", "subscribe", "sign up", "start", "try"]):
        return "high_intent"

    return "general"
