# Nama : Radhia Aulia Nisa
# NIM  : 23343049
# Prodi: Informatika

import heapq

class Graf:
    def __init__(self, jumlah_simpul):
        self.J = jumlah_simpul
        self.graf = [[0 for _ in range(jumlah_simpul)] for _ in range(jumlah_simpul)]

    def cetakMST(self, MST_edges):
        print("Sisi \tBobot")
        total_bobot = 0
        for u, v, w in MST_edges:
            print(f"{chr(97 + u)} - {chr(97 + v)} \t {w}")
            total_bobot += w
        print("Total bobot:", total_bobot)

    def primMST(self):
        MST_edges = []
        visited = [False] * self.J
        pq = [(0, 0, -1)]  # (bobot, simpul saat ini, induk)

        while pq and len(MST_edges) < self.J - 1:
            weight, u, parent = heapq.heappop(pq)

            if visited[u]:
                continue

            visited[u] = True

            if parent != -1:
                MST_edges.append((parent, u, weight))

            for v in range(self.J):
                if self.graf[u][v] > 0 and not visited[v]:
                    heapq.heappush(pq, (self.graf[u][v], v, u))

        self.cetakMST(MST_edges)

if __name__ == '__main__':
    g = Graf(9)  # Graf dengan 9 simpul (a-i)
    
    # Matriks ketetanggaan
    g.graf = [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # a
              [4, 0, 8, 0, 0, 0, 0, 11, 0], # b
              [0, 8, 0, 7, 0, 4, 0, 0, 2],  # c
              [0, 0, 7, 0, 9, 14, 0, 0, 0], # d
              [0, 0, 0, 9, 0, 10, 0, 0, 0], # e
              [0, 0, 4, 14, 10, 0, 2, 0, 0],# f
              [0, 0, 0, 0, 0, 2, 0, 1, 6],  # g
              [8, 11, 0, 0, 0, 0, 1, 0, 7], # h
              [0, 0, 2, 0, 0, 0, 6, 7, 0]]  # i

    g.primMST()
