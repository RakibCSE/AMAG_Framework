import unittest
import numpy as np
import tempfile
import os


class CommonTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = os.path.join(self.temp_dir.name, "test_data.npy")

        # Save test data to data path
        np.save(
            self.data_path,
            np.array(
                [
                    [1, 1, 10, 20],
                    [2, 1, 12, 18],
                    [3, 2, 15, 25],
                    [4, 2, 16, 24],
                    [5, 3, 5, 10],
                    [6, 4, 8, 16],
                    [7, 4, 10, 18],
                ]
            ),
        )

    def tearDown(self):
        self.temp_dir.cleanup()
