from typing import TypedDict, List, Dict, Any
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    messages: List[BaseMessage]
    metadata: Dict[str, Any]
