import numpy as np


class VehicleData:
    def __init__(self, filepath) -> None:
        self.data: np.ndarray = np.load(filepath)

    def get_data_by_id(self, _id):
        """Returns filtered data by id

        Args:
            _id (int): Id for which the data segment will be retrieved

        Returns:
            np.ndarray: Filtered data by id
        """
        filtered_data: np.ndarray = self.data[self.data[:, 1] == _id]
        return filtered_data

    def filter(self, filter_func=None):
        """Filters the data segments by filter function

        Args:
            filter_func (callable, optional): Function that takes segment as argument.

        Returns:
            list: A list contains filtered data segments.
        """

        # Check if any filter function is provided
        if filter_func is None:
            return self.data

        segments = []

        for _id in np.unique(self.data[:, 1]):
            segment = self.get_data_by_id(_id)

            # Check the segment length
            if filter_func(segment):
                segments.append(segment)

        return segments
