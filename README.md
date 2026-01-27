# defender-kql-threat-analytics

## About
Visualizes Microsoft Defender threat data (exported via KQL) as a bar graph using Python. Useful for quickly summarizing and analyzing number of stopped email threats.

> Note: This project was created as a personal tool to visualize threat data at work. The included CSV contains synthetic sample data for demonstration purposes; no real or sensitive data is included.

### Features
- Reads CSV files exported from Microsoft Defender
- Counts threats by type (e.g., Phish, Spam, Malware)
- Generates a bar graph showing the number of stopped threat emails
- Optionally generates a stacked bar graph to include delivered emails
- Displays total counts of stopped and delivered emails on the chart
- Saves the graph as an image file (.png)

### Requirements
- Python 3.x
- pandas
- matplotlib

## How to Run
1. Export email threat data from Microsoft Defender using a KQL query and save it as a CSV file.
2. Clone this repository and navigate to the project directory.
3. Install dependencies (if not already installed):
   
  ```
  pip install pandas matplotlib
  ```
  
4. Run the script:
   
  ```
  python plot.py
  ```
  
5. When prompted, enter the CSV filename and choose whether to include delivered emails in the visualization.

## Purpose
This project is a small demonstration of reading exported security data and visualizing it in Python. It is beginner-friendly but still shows practical skills in scripting, data handling, and cybersecurity reporting. 
