
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
          # Création d’un fichier terrain temporaire
        contenu = ["E..\n","CCC\n"]

        with open("terrain_test.txt", "w") as f:
            f.writelines(contenu)

        t = Terrain()
        t.charger("terrain_test.txt")

        self.assertEqual(t.cases[0][0], Case.ENTREE)
        self.assertEqual(t.cases[0][1], Case.VIDE)
        self.assertEqual(t.cases[1][0], Case.CLIENT)
        self.assertEqual(t.cases[1][2], Case.CLIENT)
        

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

