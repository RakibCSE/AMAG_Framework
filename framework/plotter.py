import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(segments):
        """_summary_

        Args:
            segments (_type_): _description_
        """
        plt.figure(figsize=(10, 6))
        plt.xlabel("Longitude (x)")
        plt.ylabel("Latitude (y)")

        for segment in segments:
            plt.plot(
                segment[:, 3],
                segment[:, 2],
            )  # Column 2 is latitude (y) and Column 3 in longitude (x)

        plt.show()
