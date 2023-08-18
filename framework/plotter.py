import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot_segments(filtered_segments: list) -> None:
        """Plot the filtered segments

        Args:
            filtered_segments (list): List of filtered segments

        Returns:
            None
        """
        plt.figure(figsize=(10, 6))
        plt.xlabel("Latitude (x)")
        plt.ylabel("Longitude (y)")

        for segment in filtered_segments:
            # Plot latitude (x, column 2) and  longitude (y, column 3)
            plt.plot(
                segment[:, 2],
                segment[:, 3],
            )

        plt.show()
