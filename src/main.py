# src/main.py
from agent.graph import build_graph

def main():
    graph = build_graph()
    graph.invoke({})

if __name__ == "__main__":
    main()
