import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(segments: list) -> None:
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
            # Plot longitude (x, column 3) and  latitude (y, column 2)
            plt.plot(
                segment[:, 3],
                segment[:, 2],
            )

        plt.show()
