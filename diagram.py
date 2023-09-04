import csv
import matplotlib.pyplot as plt
import matplotlib
from ing_theme_matplotlib import mpl_style
mpl_style(dark=False)
matplotlib.use('TkAgg')

class DIAGRAM:
    def run(self):
        # Read the results from the CSV file
        iterations = []
        loading_times = []
        element_times = []
        with open('results.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                iterations.append(int(row[0]))
                loading_times.append(float(row[1]))
                element_times.append(float(row[2]))  # Read the additional column

        # Calculate the average loading time
        avg_loading_time = sum(loading_times) / len(loading_times)
        avg_element_time = sum(element_times) / len(element_times)  # Calculate the average element time

        # Plot the loading times for each iteration
        fig, (ax1, ax2) = plt.subplots(2)
        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Performance Measure App Diagram')
        ax1.plot(iterations, loading_times, 'tab:orange' ,marker='o', label='Loading Time')
        ax1.axhline(y=avg_loading_time, color='r', linestyle='--', label='Average Loading Time')
        ax1.set_title('Page Loading Time')
        ax1.set(xlabel='Iteration', ylabel='Time (seconds)')
        ax2.plot(iterations, element_times, 'tab:blue', marker='o', label='Element Time')
        ax2.axhline(y=avg_element_time, color='g', linestyle='--', label='Average Element Time')
        ax2.set_title('Element Loading Time')
        ax2.set(xlabel='Iteration', ylabel='Time (seconds)')

        ax1.label_outer()
        ax2.label_outer()

        fig.legend(bbox_to_anchor=(1.015, 0.9), loc='right')
        fig.set_size_inches(7, 5)
        fig.tight_layout(pad=2.5)
        plt.show()


