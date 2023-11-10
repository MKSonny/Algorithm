import graphviz


def all_sum_of_subsets(S, M):
    graph = graphviz.Digraph(comment='DFS Sum of Subsets')
    DFS_sum_of_subsets(S, M, 0, [], sum(S), graph)
    return graph


def DFS_sum_of_subsets(S, M, level, sol, remaining, graph):
    node_id = f"{level}-{remaining}"
    graph.node(node_id, label=f"Level {level}\nRemaining {remaining}\nSubset {sol}")

    if sum(sol) == M:
        graph.node(f"{node_id}-M", label=f"Subset Sum is M: {sol}", shape="box")
        graph.edge(node_id, f"{node_id}-M")
        return

    if sum(sol) > M or (remaining + sum(sol)) < M:
        graph.node(f"{node_id}-Prune", label="Prune", shape="box")
        graph.edge(node_id, f"{node_id}-Prune")
        return

    for i in range(level, len(S)):
        sol.append(S[i])
        child_id = f"{level + 1}-{remaining - S[i]}"
        graph.edge(node_id, child_id)
        DFS_sum_of_subsets(S, M, i + 1, sol, remaining - S[i], graph)
        sol.pop()


# Example usage
nums = [3, 34, 4, 12, 5, 2]
M = 9
graph = all_sum_of_subsets(nums, M)

# Save the graph as a PDF file
graph.render(filename='dfs_sum_of_subsets', format='pdf', cleanup=True)