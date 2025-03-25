
import matplotlib.pyplot as plt
from IPython.display import clear_output

# Draw the CPU and memory grap
def draw_graphs(timestamps, cpu_data, memory_data):
    clear_output(wait=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
 # Plot CPU usage graph
    ax1.plot(timestamps, cpu_data, color='blue', label='CPU %')
    ax1.set_title('CPU Usage Right Now')
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('CPU (%)')
    ax1.legend(loc='upper right')

    ax2.plot(timestamps, memory_data, color='red', label='Memory %')
    ax2.set_title('Memory Usage Right Now')
    ax2.set_xlabel('Time (sec)')
    ax2.set_ylabel('Memory (%)')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Dummy test data
    timestamps = [0, 1, 2]
    cpu_data = [50, 60, 55]
    memory_data = [70, 75, 72]
    draw_graphs(timestamps, cpu_data, memory_data)
