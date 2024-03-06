import unittest
from kcs7050303 import check_logs

class TestScript(unittest.TestCase):
    def test_check_logs_no_errors(self):
        # Test when there are no errors in the log file
        log_file = 'test_logs_no_errors.log'
        with open(log_file, 'w') as f:
            f.write("No errors found in logs.")
        self.assertEqual(check_logs(log_file), [])

    def test_check_logs_with_errors(self):
        # Test when there are errors in the log file
        log_file = 'test_logs_with_errors.log'
        with open(log_file, 'w') as f:
            f.write("ERROR: could not find ovs-if-br-ex conn file after cloning")
        self.assertEqual(check_logs(log_file), ["ERROR: could not find ovs-if-br-ex conn file after cloning"])

if __name__ == '__main__':
    unittest.main()
