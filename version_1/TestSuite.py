import unittest
from Tests.Test_login_page import TestLoginPage
from Links import Links

for i in Links.CHECK_LINKS:
    print()
    print(i)
    TestLoginPage.URL = i
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLoginPage))
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

