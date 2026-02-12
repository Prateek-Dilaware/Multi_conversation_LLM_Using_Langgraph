from state import GraphState
from llm_client import get_llm

from langchain_core.messages import AIMessage


llm = get_llm()


def llm_node(state: GraphState) -> GraphState:
    """
    Message-aware LLM node.
    Reads full conversation history,
    sends to LLM,
    appends AI response,
    returns updated state.
    """

    messages = state["messages"]
    metadata = state["metadata"]

    # Call LLM with full conversation history
    response = llm.invoke(messages)

    # Ensure response is AIMessage
    ai_message = AIMessage(content=response.content)

    # Append AI message to history
    updated_messages = messages + [ai_message]

    return {
        "messages": updated_messages,
        "metadata": metadata
    }
