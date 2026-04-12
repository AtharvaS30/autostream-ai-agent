from agent import Agent

agent = Agent()

print("AutoStream AI Agent 🤖 (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.respond(user_input)
    print("Agent:", response)
