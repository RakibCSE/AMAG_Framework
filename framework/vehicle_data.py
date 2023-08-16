import numpy as np

class VehicleData:
    def __init__(self, filepath) -> None:
        self.data: np.ndarray = np.load(filepath)
    
    def get_data_by_id(self, _id):
        """Returns filtered data by id

        Args:
            _id (int):

        Returns:
            filtered_data (np.ndarray): Filtered data by id
        """
        filtered_data: np.ndarray = self.data[self.data[:, 1] == _id]
        return filtered_data
    