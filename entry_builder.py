import uuid
import time

from langchain_core.messages import HumanMessage, SystemMessage

from state import GraphState


SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly, accurately, and concisely.
If you are unsure, say you are unsure.
"""


def build_initial_state(user_input: str) -> GraphState:
    """
    Converts raw user input into production-ready GraphState.
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT.strip()),
        HumanMessage(content=user_input)
    ]

    metadata = {
        "session_id": str(uuid.uuid4()),
        "request_timestamp": time.time(),
        "model": "gemini-2.5-flash"
    }

    return {
        "messages": messages,
        "metadata": metadata
    }
