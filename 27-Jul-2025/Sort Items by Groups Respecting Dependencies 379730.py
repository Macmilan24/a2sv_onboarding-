# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for i in range(n):
            for prev in beforeItems[i]:
                item_graph[prev].append(i)
                item_indegree[i] += 1
                if group[prev] != group[i]:  
                    group_graph[group[prev]].append(group[i])
                    group_indegree[group[i]] += 1

        def topo_sort(graph, indegree, nodes):
            queue = deque()
            for node in nodes:
                if indegree[node] == 0:
                    queue.append(node)
            result = []
            while queue:
                curr = queue.popleft()
                result.append(curr)
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return result if len(result) == len(nodes) else []

        all_items = list(range(n))
        all_groups = list(range(m))

        item_order = topo_sort(item_graph, item_indegree, all_items)
        group_order = topo_sort(group_graph, group_indegree, all_groups)

        if not item_order or not group_order:
            return []

        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)

        result = []
        for grp in group_order:
            result.extend(group_to_items[grp])

        return result