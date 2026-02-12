from langgraph.graph import StateGraph, END

from state import GraphState
from nodes import llm_node


def build_graph():
    graph = StateGraph(GraphState)
     
     
    #nodes 
    graph.add_node("llm_node", llm_node) 
     
    #edges 
    graph.set_entry_point("llm_node") # start with LLM node, which will read initial user message from state

    graph.add_edge("llm_node", END) # end after LLM response, for simplicity. In a more complex graph, we could have multiple nodes and edges.

    return graph.compile()
