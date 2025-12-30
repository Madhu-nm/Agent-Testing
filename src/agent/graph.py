# src/agent/graph.py
from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.nodes import (
    fetch_prs,
    extract_jira,
    generate_notes,
    write_release_notes,
)

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("fetch_prs", fetch_prs.run)
    graph.add_node("extract_jira", extract_jira.run)
    graph.add_node("generate_notes", generate_notes.run)
    graph.add_node("write_release_notes", write_release_notes.run)

    graph.set_entry_point("fetch_prs")
    graph.add_edge("fetch_prs", "extract_jira")
    graph.add_edge("extract_jira", "generate_notes")
    graph.add_edge("generate_notes", "write_release_notes")

    return graph.compile()
