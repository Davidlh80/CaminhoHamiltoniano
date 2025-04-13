def input_graph():
    print("### Caminho Hamiltoniano ###")
    is_directed = input("O grafo é orientado? (s/n): ").strip().lower() == 's'

    n = int(input("Número de vértices: "))
    m = int(input("Número de arestas: "))

    graph = {i: [] for i in range(n)}

    print("Digite as arestas (formato: u v):")
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        if not is_directed:
            graph[v].append(u)

    return graph, n


def hamiltonian_path(graph, n):
    def backtrack(path, visited):
        if len(path) == n:
            return path

        current = path[-1]
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                result = backtrack(path, visited)
                if result:
                    return result
                path.pop()
                visited[neighbor] = False

        return None

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path = [start]
        result = backtrack(path, visited)
        if result:
            return result

    return None


def main():
    graph, n = input_graph()
    path = hamiltonian_path(graph, n)

    if path:
        print("Caminho Hamiltoniano encontrado:")
        print(path)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")


if __name__ == "__main__":
    main()
