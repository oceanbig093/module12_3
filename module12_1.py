import unittest
import runnerfirst

def frozen(func):
    def wrapper(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func
    return wrapper


class TestRunner(unittest.TestCase):
    is_frozen = False
    @frozen
    def test_walk(self):
        walker = runnerfirst.Runner('ходок')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @frozen
    def test_run(self):
        run = runnerfirst.Runner('бегун')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @frozen
    def test_challenge(self):
        challenger1 = runnerfirst.Runner('соп1')
        challenger2 = runnerfirst.Runner('соп2')
        for i in range(10):
            challenger2.run()
            challenger1.walk()
        self.assertNotEqual(challenger1.distance, challenger2.distance)


if __name__ == '__name__':
    unittest.main()
