import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(segments):
        """Plot the filtered segments

        Args:
            segments (list): List of segments

        Returns:
            None
        """
        plt.figure(figsize=(10, 6))
        plt.xlabel("Longitude (x)")
        plt.ylabel("Latitude (y)")

        for segment in segments:
            plt.plot(
                segment[:, 3],
                segment[:, 2],
            )  # Column 3 is longitude (x) and Column 2 in latitude (y)

        plt.show()
