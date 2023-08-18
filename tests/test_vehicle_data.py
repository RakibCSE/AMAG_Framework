import numpy as np

from test_utils import CommonTest
from framework.vehicle_data import VehicleData


def length_filter(segment) -> bool:
    return len(segment) > 1


class TestVehicleData(CommonTest):
    def test_get_data_by_id(self) -> None:
        obj = VehicleData(self.data_path)
        result = obj.get_data_by_id(1)
        expected = np.array([[1, 1, 10, 20], [2, 1, 12, 18]])
        self.assertTrue(np.array_equal(result, expected))

    def test_filter(self) -> None:
        obj = VehicleData(self.data_path)
        filtered_segments = obj.filter(filter_func=length_filter)

        # Check if all the segments length condition
        for segment in filtered_segments:
            self.assertTrue(length_filter(segment))

        # Check the number of segments in correct
        self.assertEqual(len(filtered_segments), 3)
