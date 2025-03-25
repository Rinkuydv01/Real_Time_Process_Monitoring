#module 1
import psutil
import time

# Lists to store data
timestamps = []
cpu_data = []
memory_data = []
random_extra_list = []

# Variables for monitoring
total_time = 60
wait_time = 1
max_points = total_time

# Collect data for the dashboard
def collect_data():
    for sec in range(total_time):
        try:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent

            timestamps.append(sec)
            cpu_data.append(cpu)
            memory_data.append(mem)
            random_extra_list.append(cpu * 2)  # Dummy processing

            if len(timestamps) > max_points:
                timestamps.pop(0)
                cpu_data.pop(0)
                memory_data.pop(0)

            # Return data for other modules to use
            yield sec, cpu, mem

        except Exception as oops:
            print(f"Error happened: {oops}")

if __name__ == "__main__":
    print("Starting data collection...")
    for sec, cpu, mem in collect_data():
        print(f"Time: {sec}, CPU: {cpu}%, Memory: {mem}%")
