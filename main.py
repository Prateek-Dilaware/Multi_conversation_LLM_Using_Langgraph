from graph_builder import build_graph
from entry_builder import build_initial_state
from conversation_manager import append_user_message


EXIT_COMMANDS = {"exit", "quit", "bye"}


def run_conversation():

    app = build_graph()

    print("\n=== Chat Session Started ===")
    print("Type 'exit', 'quit', or 'bye' to end.\n")

    # First turn
    user_input = input("You: ").strip()

    if user_input.lower() in EXIT_COMMANDS:
        print("Session ended.")
        return

    state = build_initial_state(user_input)

    result = app.invoke(state)
    state = result

    print("\nAI:", state["messages"][-1].content, "\n")

    # Multi-turn loop
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in EXIT_COMMANDS:
            print("\n=== Chat Session Ended ===")
            break

        state = append_user_message(state, user_input)

        result = app.invoke(state)
        state = result

        print("\nAI:", state["messages"][-1].content, "\n")


if __name__ == "__main__":
    run_conversation()
