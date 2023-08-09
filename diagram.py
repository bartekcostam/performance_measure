import csv
import matplotlib.pyplot as plt
import matplotlib
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
        plt.plot(iterations, loading_times, marker='o', label='Loading Time')
        plt.plot(iterations, element_times, marker='x', label='Element Time')  # Plot the element times
        plt.axhline(y=avg_loading_time, color='r', linestyle='--', label='Average Loading Time')
        plt.axhline(y=avg_element_time, color='g', linestyle='--', label='Average Element Time')  # Plot the average element time
        plt.xlabel('Iteration')
        plt.ylabel('Time (seconds)')
        plt.title('Web Page Loading Speed Test')
        plt.legend()
        plt.show()
