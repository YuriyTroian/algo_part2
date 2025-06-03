import csv, os


class DeliveryNetwork:
    def __init__(self):
        self.graph = {}
        self.sources = []
        self.sinks = []

    def load_from_csv(self, filepath: str):
        with open(filepath, newline="") as csvfile:
            reader = list(csv.reader(csvfile))
            self.sources = reader[0]
            self.sinks = reader[1]

            for line in reader[2:]:
                u, v, capacity = line
                capacity = int(capacity)
                if u not in self.graph:
                    self.graph[u] = {}
                self.graph[u][v] = capacity
                if v not in self.graph:
                    self.graph[v] = {}

    def _bfs(self, residual, parent, source, sink):
        visited = set()
        queue = [source]
        visited.add(source)

        while queue:
            u = queue.pop(0)  # emulate queue with list
            for v in residual.get(u, {}):
                if v not in visited and residual[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def max_flow(self):
        super_source = "SS"
        super_sink = "TT"

        if super_source not in self.graph:
            self.graph[super_source] = {}
        for src in self.sources:
            self.graph[super_source][src] = float("inf")

        for sink in self.sinks:
            if sink not in self.graph:
                self.graph[sink] = {}
            self.graph[sink]["TT"] = float("inf")

        residual = {}
        for u in self.graph:
            residual[u] = {}
            for v in self.graph[u]:
                residual[u][v] = self.graph[u][v]
                if v not in residual:
                    residual[v] = {}
                if u not in residual[v]:
                    residual[v][u] = 0

        max_flow = 0
        parent = {}

        while self._bfs(residual, parent, super_source, super_sink):
            path_flow = float("inf")
            s = super_sink
            while s != super_source:
                path_flow = min(path_flow, residual[parent[s]][s])
                s = parent[s]

            v = super_sink
            while v != super_source:
                u = parent[v]
                residual[u][v] -= path_flow
                if u not in residual[v]:
                    residual[v][u] = 0
                residual[v][u] += path_flow
                v = u

            max_flow += path_flow
            parent = {}

        return int(max_flow)
network = DeliveryNetwork()
file_path = os.path.join(os.path.dirname(__file__), "../roads.csv")
network.load_from_csv(file_path)
print(network.max_flow())

import csv, os


# import csv, os
#
#
# class DeliveryNetwork:
#     def __init__(self):
#         self.graph = {}
#         self.sources = []
#         self.sinks = []
#
#     def load_from_csv(self, filepath: str):
#         with open(filepath, newline="") as csvfile:
#             reader = list(csv.reader(csvfile))
#             self.sources = reader[0]
#             self.sinks = reader[1]
#
#             for line in reader[2:]:
#                 u, v, capacity = line
#                 capacity = int(capacity)
#                 if u not in self.graph:
#                     self.graph[u] = {}
#                 self.graph[u][v] = capacity
#                 if v not in self.graph:
#                     self.graph[v] = {}
#
#         print(" Початковий граф:")
#         self._print_graph(self.graph)
#
#     def _bfs(self, residual, parent, source, sink):
#         visited = set()
#         queue = [source]
#         visited.add(source)
#
#         while queue:
#             u = queue.pop(0)
#             for v in residual.get(u, {}):
#                 if v not in visited and residual[u][v] > 0:
#                     visited.add(v)
#                     parent[v] = u
#                     if v == sink:
#                         return True
#                     queue.append(v)
#         return False
#
#     def max_flow(self):
#         super_source = "SS"
#         super_sink = "TT"
#
#         if super_source not in self.graph:
#             self.graph[super_source] = {}
#         for src in self.sources:
#             self.graph[super_source][src] = float("inf")
#
#         for sink in self.sinks:
#             if sink not in self.graph:
#                 self.graph[sink] = {}
#             self.graph[sink][super_sink] = float("inf")
#
#         residual = {}
#         for u in self.graph:
#             residual[u] = {}
#             for v in self.graph[u]:
#                 residual[u][v] = self.graph[u][v]
#                 if v not in residual:
#                     residual[v] = {}
#                 if u not in residual[v]:
#                     residual[v][u] = 0
#
#         original = {u: dict(v) for u, v in self.graph.items()}
#         max_flow = 0
#         parent = {}
#
#         while self._bfs(residual, parent, super_source, super_sink):
#             path_flow = float("inf")
#             s = super_sink
#             while s != super_source:
#                 path_flow = min(path_flow, residual[parent[s]][s])
#                 s = parent[s]
#
#             v = super_sink
#             while v != super_source:
#                 u = parent[v]
#                 residual[u][v] -= path_flow
#                 if u not in residual[v]:
#                     residual[v][u] = 0
#                 residual[v][u] += path_flow
#                 v = u
#
#             max_flow += path_flow
#             parent = {}
#
#         print("\n Пропущений потік по ребрах:")
#         self._print_flow(original, residual)
#
#         return int(max_flow)
#
#     def _print_graph(self, graph):
#         for u in graph:
#             for v in graph[u]:
#                 print(f"{u} → {v} : {graph[u][v]}")
#
#     def _print_flow(self, original, residual):
#         for u in original:
#             for v in original[u]:
#                 if u in residual and v in residual[u]:
#                     flow = original[u][v] - residual[u][v]
#                     if original[u][v] != float("inf"):
#                         print(f"{u} → {v} : {flow}/{original[u][v]}")
#
#
#
# network = DeliveryNetwork()
# file_path = os.path.join(os.path.dirname(__file__), "../roads.csv")
# network.load_from_csv(file_path)
# print(f"\n Максимальний потік: {network.max_flow()}")




#
# dn = DeliveryNetwork()
# print(dn.load_from_csv("roads.csv"))