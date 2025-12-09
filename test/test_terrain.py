
import unittest
import xmlrunner
import os
from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        
    # Création d'un fichier temporaire pour le test
        fichier_test = "terrain_test.txt"
        with open(fichier_test, "w") as f:
            f.write("E~ \nC C\n~~C\n")

        t = Terrain()
        t.charger(fichier_test)

        # Vérification de la taille
        self.assertEqual(t.largeur, 3)
        self.assertEqual(t.hauteur, 3)

        # Vérification du contenu
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[0][2], Case.OBSTACLE)
        self.assertEqual(t[1][0], Case.CLIENT)
        self.assertEqual(t[1][1], Case.OBSTACLE)
        self.assertEqual(t[1][2], Case.CLIENT)
        self.assertEqual(t[2][0], Case.VIDE)
        self.assertEqual(t[2][1], Case.VIDE)
        self.assertEqual(t[2][2], Case.CLIENT)

        # Vérification des méthodes get_clients et get_entree
        self.assertEqual(t.get_entree(), (0, 0))
        self.assertEqual(t.get_clients(), [(1, 0), (1, 2), (2, 2)])

        # Suppression du fichier temporaire
        os.remove(fichier_test)

        self.fail()

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

