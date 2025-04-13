# Caminho Hamiltoniano

Um **Caminho Hamiltoniano** em um grafo é um caminho que visita **cada vértice exatamente uma vez**. Este projeto implementa uma abordagem em Python para determinar se um caminho hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo.

---

## Explicando o Algoritmo

A implementação utiliza uma abordagem de **backtracking** com verificação de todos os caminhos possíveis a partir de cada vértice inicial.

```python
def hamiltonian_path(graph, n):
```
- Função principal que recebe o grafo (como dicionário de adjacência) e o número de vértices `n`.

```python
    def backtrack(path, visited):
```
- Função auxiliar recursiva. Recebe o caminho atual (`path`) e um vetor booleano (`visited`) que indica quais vértices já foram visitados.

```python
        if len(path) == n:
            return path
```
- Caso base: se o comprimento do caminho for igual ao número total de vértices, um Caminho Hamiltoniano foi encontrado e ele é retornado.

```python
        current = path[-1]
```
- Pega o último vértice inserido no caminho, pois a próxima busca será a partir dele.

```python
        for neighbor in graph[current]:
```
- Itera sobre todos os vizinhos do vértice atual.

```python
            if not visited[neighbor]:
```
- Verifica se o vizinho ainda **não foi visitado** (importante para garantir que cada vértice seja visitado apenas uma vez).

```python
                visited[neighbor] = True
                path.append(neighbor)
```
- Marca o vizinho como visitado e o adiciona ao caminho atual.

```python
                result = backtrack(path, visited)
```
- Chama a função recursivamente para continuar a busca a partir desse novo caminho.

```python
                if result:
                    return result
```
- Se a chamada recursiva retornar um caminho válido, ele é imediatamente retornado para interromper a busca.

```python
                path.pop()
                visited[neighbor] = False
```
- **Backtracking**: se não for possível formar um caminho a partir do vizinho atual, desfaz as alterações feitas (remove o vértice e marca como não visitado) para tentar outras opções.

```python
        return None
```
- Nenhum caminho válido encontrado a partir do vértice atual. Retorna `None` para continuar a busca por outras rotas possíveis.

```python
    for start in range(n):
```
- Tenta iniciar o caminho a partir de **cada vértice** do grafo, já que um Caminho Hamiltoniano pode começar de qualquer vértice.

```python
        visited = [False] * n
        visited[start] = True
        path = [start]
```
- Inicializa o vetor de visitados e define o caminho inicial com o vértice atual (`start`).

```python
        result = backtrack(path, visited)
        if result:
            return result
```
- Inicia o processo de busca e retorna o primeiro caminho Hamiltoniano encontrado.

```python
    return None
```
- Caso nenhum caminho seja encontrado partindo de nenhum vértice, retorna `None`.

---

## Como executar

### Requisitos
Python 3.x instalado

### Passo 1: Clone o repositório
```bash
git clone https://github.com/Davidlh80/CaminhoHamiltoniano.git
cd CaminhoHamiltoniano
```

### Passo 2: Execute o script
```bash
python main.py
```

O programa solicitará as seguintes entradas:

1. Se o grafo é orientado (`s` para sim, `n` para não)
2. Número de vértices
3. Número de arestas
4. As arestas no formato `u v`

---

## Exemplo de execução

```
O grafo é orientado? (s/n): n
Número de vértices: 4
Número de arestas: 5
Digite as arestas (formato: u v):
0 1
0 2
1 2
1 3
2 3
Caminho Hamiltoniano encontrado:
[0, 1, 2, 3]
```

---

## Análise da Complexidade Computacional

### Classes de Problemas

Antes de analisar a complexidade do problema do Caminho Hamiltoniano, é importante entender as classes de problemas computacionais:

- **Classe P**: Conjunto de problemas que podem ser resolvidos em tempo polinomial por um algoritmo determinístico. Esses problemas são considerados "fáceis" ou "eficientemente resolvíveis".

- **Classe NP**: Conjunto de problemas cuja solução pode ser verificada em tempo polinomial por um algoritmo determinístico. Ou seja, se alguém fornecer uma solução, é possível verificar rapidamente se ela está correta.

- **Classe NP-Completo**: Subconjunto de problemas em NP que são os mais difíceis dentro dessa classe. Um problema é NP-Completo se:
    1. Ele pertence à classe NP.
    2. Qualquer outro problema em NP pode ser reduzido a ele em tempo polinomial.

- **Classe NP-Difícil**: Conjunto de problemas que são pelo menos tão difíceis quanto os problemas NP-Completo. Esses problemas não precisam necessariamente pertencer à classe NP (ou seja, suas soluções podem não ser verificáveis em tempo polinomial).

### O Problema do Caminho Hamiltoniano

O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**. Isso significa que:

- A verificação de uma solução (ou seja, verificar se um caminho dado é Hamiltoniano) pode ser feita em tempo polinomial.
- Qualquer outro problema em NP pode ser reduzido ao problema do Caminho Hamiltoniano em tempo polinomial.

A resolução eficiente (em tempo polinomial) de um problema NP-Completo, como o Caminho Hamiltoniano, implicaria que **P = NP**, o que é uma das maiores questões em aberto da ciência da computação teórica.

---

## Complexidade Assintótica de Tempo

- **Pior caso**: O algoritmo explora todas as `n!` permutações possíveis dos vértices – **O(n!)**
- **Melhor caso**: Encontra um caminho logo nas primeiras tentativas – **O(n)**
- **Caso médio**: Depende da estrutura do grafo e pode também ser **O(n!)**

> O algoritmo não se enquadra no Teorema Mestre, pois não divide o problema em subproblemas de tamanho `n/b`, como ocorre em algoritmos do tipo *divide-and-conquer*.

---

## Análise dos Casos

| Caso           | Descrição                                                                 | Complexidade  |
|----------------|---------------------------------------------------------------------------|---------------|
| Melhor caso    | Caminho encontrado logo no início, sem backtracking                       | O(n)          |
| Caso médio     | Algumas tentativas e backtracking, dependendo da estrutura do grafo       | O(n!)         |
| Pior caso      | Exploração completa de todas permutações possíveis sem sucesso            | O(n!)         |

---

## Observações

- Como o algoritmo é baseado em força bruta (backtracking), ele **não é indicado para grafos grandes**.
