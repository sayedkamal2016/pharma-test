import unittest
from version_1.Tests.Test_login_page import TestLoginPage


class MyTestCase(unittest.TestSuite):
    result = unittest.TestResult()
    result.startTest(TestLoginPage)


if __name__ == '__main__':
    unittest.main()
