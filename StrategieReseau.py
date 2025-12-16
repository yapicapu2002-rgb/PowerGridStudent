
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []

        nb = int(input("Nombre de noeuds : "))

        for i in range(nb):
            x = int(input(f"Noeud {i} - ligne : "))
            y = int(input(f"Noeud {i} - colonne : "))
            noeuds[i] = (x, y)

        entree = int(input("Id du noeud d'entrée : "))

        nb_arcs = int(input("Nombre d'arcs : "))
        for _ in range(nb_arcs):
            a = int(input("Arc - noeud 1 : "))
            b = int(input("Arc - noeud 2 : "))
            arcs.append((a, b))

    return entree, noeuds, arcs
        

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []

        id_noeud = 0
        entree = -1
        coord_to_id = {}

        # Création des noeuds
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case != Case.OBSTACLE:
                    noeuds[id_noeud] = (i, j)
                    coord_to_id[(i, j)] = id_noeud
                    if case == Case.ENTREE:
                        entree = id_noeud
                    id_noeud += 1

        # Création des arcs (voisins)
        for (i, j), n1 in coord_to_id.items():
            for di, dj in [(1, 0), (0, 1)]:
                voisin = (i + di, j + dj)
                if voisin in coord_to_id:
                    n2 = coord_to_id[voisin]
                    arcs.append((n1, n2))

     return entree, noeuds, arcs

