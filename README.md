# Real-Time Process Monitoring Dashboard

This repository contains our project for the CSE316 course at Lovely Professional University, submitted as part of Academic Task-2. Our team developed a Real-Time Process Monitoring Dashboard to track a computer’s CPU and memory usage in real-time, visualize the data through graphs, and issue alerts if usage exceeds safe thresholds. The project is implemented in Python and divided into three distinct modules, each handled by a team member. This tool is designed to help system administrators monitor system performance and identify potential issues quickly.

## Project Overview
The Real-Time Process Monitoring Dashboard is a Python-based application that provides live monitoring of system resources. It collects CPU and memory usage data every second for a specified duration (default: 60 seconds), displays the data in graphical form, and issues alerts if usage levels become critical. Key features include:
- **Real-Time Data Collection:** Gathers CPU and memory usage percentages every second.
- **Live Visualization:** Displays usage trends in graphs (CPU in blue, memory in red).
- **Monitoring and Alerts:** Issues warnings if CPU or memory usage exceeds predefined thresholds, logs alerts, and calculates statistical metrics like averages, maximum, and minimum values.
- **Modular Design:** Split into three independent modules for better collaboration and maintainability.

## What It Does
- Collects CPU and memory usage data every second for 60 seconds (configurable duration).
- Visualizes the data in real-time using line graphs (CPU usage in blue, memory usage in red).
- Monitors usage levels and issues alerts:
  - CPU > 80%: “Alert: CPU usage is critically high.”
  - CPU > 55%: “Notice: CPU usage is moderately high.”
  - Memory > 75%: “Alert: Memory usage is critically high.”
  - Memory > 50%: “Notice: Memory usage is moderately high.”
- Calculates and displays average, maximum, and minimum CPU and memory usage.
- Logs all alerts and provides a summary at the end of the monitoring session.

## How to Run It
Follow these steps to set up and run the project on your system:
1. **Install Python 3:**
   - Download and install Python 3 from [python.org](https://www.python.org/downloads/) 
   - Ensure Python is added to your system’s PATH.
2. **Install Required Libraries:**
   - Open a terminal or command prompt.
   - Run the following command to install the necessary Python libraries:
  
3. **Clone or Download the Repository:**
- Clone this repository using Git:
- Or download the ZIP file from GitHub and extract it.
4. **Navigate to the Project Directory:**
- Open a terminal and change to the project directory:
- 5. **Run the Project:**
- Execute the main script to start the monitoring dashboard:
- - The dashboard will start, showing live graphs and printing usage data and alerts.
6. **Stop the Program:**
- The program runs for 60 seconds by default.
- To stop it early, press `Ctrl+C` in the terminal.

## Project Structure
The project is divided into three modules, each responsible for a specific functionality. The files are organized as follows:
- **Data Collection (`data_collection.py`):**
- Handles the collection of CPU and memory usage data using the `psutil` library.
- Collects data every second and yields the timestamp, CPU percentage, and memory percentage.
- Includes error handling to manage potential failures in data collection.
- **Visualization (`visualization.py`):**
- Generates live graphs to visualize CPU and memory usage over time.
- Uses `matplotlib` to plot CPU usage in blue and memory usage in red.
- **Monitoring & Alerts (`monitoring_alerts.py`):**
- My contribution to the project.
- Monitors CPU and memory usage levels and issues alerts based on predefined thresholds.
- Calculates statistical metrics (average, maximum, minimum) for CPU and memory usage.
- Logs all alerts in a history list and provides a summary at the end of the session.
- Features include:
- Configurable thresholds (e.g., CPU critical at 80%, memory critical at 75%).
- Timestamped alert messages for better tracking.
- A reset function to clear alert history for new sessions.
- **Main Script (`main.py`):**
- Integrates all modules to run the dashboard.
- Calls `collect_data` to gather data, `draw_graphs` to visualize it, and `cpu_check`/`memory_check` to monitor and alert.

## Team Members and Contributions
Our team consists of three members, each responsible for one module:
- **Roll Number 12345:** Developed the Data Collection module (`data_collection.py`).
- **Roll Number 67890:** Developed the Visualization module (`visualization.py`).
- **Me (Roll Number 54321):** Developed the Monitoring & Alerts module (`monitoring_alerts.py`).

*Note:* Replace the roll numbers with your team’s actual roll numbers before submission.

## Technologies Used
We used the following tools and technologies to build this project:
- **Python 3:** The programming language for the entire project.
- **Libraries:**
- `psutil`: For collecting system resource usage (CPU and memory).
- `matplotlib`: For generating live graphs to visualize usage data.
- `numpy`: Included for potential numerical computations (though minimally used).
- `IPython.display`: For updating graphs in real-time.
- `time`: For managing delays and timestamps.
- **GitHub:** For version control and collaboration.
- We used branches (`data-collection`, `visualization`, `monitoring-alerts`) to work on our modules independently.
- All changes were merged into the `main` branch after development.

## Development Process
We followed a structured workflow to develop this project:
1. **Repository Setup:**
- Created a public repository on GitHub named `RealTimeProcessMonitoring`.
- Initialized it with a blank `README.md`.
2. **Module Development:**
- Each team member created a branch for their module:
- `data-collection` for Module 1.
- `visualization` for Module 2.
- `monitoring-alerts` for Module 3 (my part).
- Developed our modules independently, making multiple commits to show progress.
3. **Revisions:**
- Made at least 7 commits across the project, as required by the assignment.
- For my module (`monitoring_alerts.py`), I made changes like adjusting thresholds, adding alert history, and enhancing the test block.
4. **Integration:**
- Merged all branches into `main` using pull requests.
- Updated `main.py` to ensure all modules work together seamlessly.
5. **Documentation:**
- Added this detailed `README.md` to explain the project, setup, and contributions.

## Notes
- The program runs for 60 seconds by default but can be configured to run for a different duration by modifying the `duration` parameter in `collect_data`.
- Alerts are issued at 80% for CPU and 75% for memory, with messages like “Alert: CPU usage is critically high.” I adjusted these thresholds from an initial 85% to make the alerts more practical.
- You can stop the program early by pressing `Ctrl+C` in the terminal.
- The Monitoring & Alerts module logs all alerts and provides a summary at the end, showing up to 5 alerts (I reduced this from 10 to avoid clutter).

## Future Improvements
We have some ideas to enhance the project in the future:
- Add the ability to monitor and display running processes that are consuming the most resources.
- Implement email or desktop notifications for critical alerts.
- Extend the monitoring duration dynamically based on user input.
- Add a user interface (e.g., using Tkinter) to make the dashboard more interactive.

## GitHub Contributions
We made 25+ commits to this repository to track our progress. You can view the commit history by clicking the “Commits” tab on GitHub. Each team member contributed through their respective branches, and all changes were merged into `main`. Check the commit messages for details on our work!

---
**Course:** CSE316  
**Institution:** Lovely Professional University  
**Date:** March 25, 2025
