from framework.vehicle_data import VehicleData
from framework.filters import length_filter
from framework.plotter import Plotter


if __name__ == "__main__":
    data_path = "./data.npy"

    # VehicleData instance
    obj = VehicleData(data_path)

    # Get data for specific Id
    id_data = obj.get_data_by_id(4)

    
    filtered_segments = obj.filter(filter_func=length_filter)

    # Create a Plotter instance
    plotter = Plotter()

    # Plot the filtered segments
    plotter.plot(filtered_segments[:50])
