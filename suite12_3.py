import unittest
import module12_2
import module12_1

tester = unittest.TestSuite()
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(module12_2.TournamentTest))
tester.addTest(unittest.TestLoader().loadTestsFromTestCase(module12_1.TestRunner))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tester)