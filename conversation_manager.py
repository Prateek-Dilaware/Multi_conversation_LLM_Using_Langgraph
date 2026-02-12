from langchain_core.messages import HumanMessage

from state import GraphState


def append_user_message(
    state: GraphState,
    user_input: str
) -> GraphState:
    """
    Appends a new HumanMessage to conversation state
    without mutating original state.
    """

    messages = state["messages"]
    metadata = state["metadata"]

    new_message = HumanMessage(content=user_input)

    updated_messages = messages + [new_message]

    return {
        "messages": updated_messages,
        "metadata": metadata
    }
