import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        man = Runner("IVAN_GAV")
        for i in range(0, 10):
            man.walk()
        self.assertEqual(man.distance, 50)

    def test_run(self):
        man = Runner("Nicola_Tesla")
        for i in range(0, 10):
            man.run()
        self.assertEqual(man.distance, 100)

    def test_challenger(self):
        man1 = Runner("ISAK")
        man2 = Runner("POLYAK")
        for i in range(0, 10):
            man1.run()
            man2.walk()
        self.assertNotEqual(man1.distance, man2.distance)


if __name__ == "__main__":
    unittest.main()
