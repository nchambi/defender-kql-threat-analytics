# defender-kql-threat-analytics

## About
Visualizes Microsoft Defender threat data (exported via KQL) as a bar graph using Python. Useful for quickly summarizing and analyzing number of stopped email threats.

> Note: This project was created as a personal tool to visualize threat data at work. The included CSV contains synthetic sample data for demonstration purposes; no real or sensitive data is included.

### Features
- Reads CSV files exported from Microsoft Defender
- Counts threats by type (e.g., Phish, Spam, Malware)
- Generates a bar graph showing threats over time
- Saves the graph as an image file (.png)

### Requirements
- Python 3.x
- pandas
- matplotlib

## Purpose
This project is a small demonstration of reading exported security data and visualizing it in Python. It is beginner-friendly but still shows practical skills in scripting, data handling, and cybersecurity reporting. 
