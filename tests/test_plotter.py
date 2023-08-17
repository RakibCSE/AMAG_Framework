from test_utils import CommonTest
from framework.vehicle_data import VehicleData
from framework.plotter import Plotter


class TestPlotter(CommonTest):
    def test_plot(self) -> None:
        obj = VehicleData(self.data_path)
        plotter = Plotter()

        # Get filtered segments
        filtered_segments = obj.filter(lambda segment: len(segment) > 1)

        # Test plot function
        plotter.plot(filtered_segments)
