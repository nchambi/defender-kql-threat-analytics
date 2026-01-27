"""
Reads Microsoft Defender CSV exports generated from a KQL query
and visualizes the number of email threats stopped using a bar graph.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# --- INPUT --- #

# Insert csv file 
while True:
    filename = input("Enter CSV filename: ").strip().strip("")

    if not filename:
        print("No file provided. Exiting.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        print("Please try again. \n")
        continue

    break

try:
    df = pd.read_csv(filename)
except Exception as e:
    print(f"Failed to read CSV: {e}")
    input("press Enter to exit...")
    sys.exit(1)

add_delivered = input("Would you like to include Delivered data? (y/n): ")

if add_delivered not in ("Y", "y", "n", "N"):
    print(f"Failed to read CSV")
    input("press Enter to try again...")
    sys.exit(1)

# --- DATA --- # 

# Specify columns from csv 
spam = df["ThreatTypes"] == "Spam"
phish = df["ThreatTypes"] == "Phish"
phish_spam = df["ThreatTypes"] == "Phish, Spam"
malware = df["ThreatTypes"] == "Malware"

# Specify which values are grouped together 
stopped = (
    (df["DeliveryAction"] == "Junked") |
    (df["DeliveryAction"] == "Quarantined") |
    (df["DeliveryAction"] == "Blocked"))

delivered = df["DeliveryAction"] == "Delivered"

empty_isNull = (df["DeliveryAction"] == " ")

# --- CALCULATE ---#

# Calculate number of emails stopped based on the threat 
Spam = (spam & stopped).sum()
Phish = (phish & stopped).sum()
Phish_spam = (phish_spam & stopped).sum()
Malware = (malware & (stopped | empty_isNull)).sum()

# Calculate number of emails delivered based on the threat 
SpamDelivered = (spam & delivered).sum()
PhishDelivered  = (phish & delivered).sum()
Phish_spamDelivered  = (phish_spam & delivered).sum()
MalwareDelivered  = (malware & delivered).sum()

# Calculate total stopped emails 
total_stopped = Spam + Phish + Phish_spam + Malware

# Calculate total delivered emails 
total_delivered = SpamDelivered + PhishDelivered + Phish_spamDelivered + MalwareDelivered

# Print second line of graph title as the date 

df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
timestamp = df["Timestamp"]
start_date = timestamp.min()
end_date = timestamp.max()
bottom_date = start_date.strftime("%b %d")
top_date = end_date.strftime("%b %d")

# --- PLOT ---#

# Create a data table
summary = pd.DataFrame({
    'Type of Threat':['Spam', 'Phish', 'Phish, Spam', 'Malware'],
    'Stopped': [Spam, Phish, Phish_spam, Malware],
    'Delivered': [SpamDelivered, PhishDelivered, Phish_spamDelivered, MalwareDelivered]
})

# Determine size of inside (ax) and outside (fig) of bar graph display 
fig, ax = plt.subplots(figsize=(8, 5))

if add_delivered in ("y", "Y"):
    # Label axis 
    ax = summary.plot.bar(
        x='Type of Threat', 
        y=['Stopped', 'Delivered'], 
        stacked = True,
        ax=ax,
        rot=0
    )

    # Display total number of emails top right outsifde (fig) of bar graph
    fig.text(
        0.98, 0.97,          
        f"{total_stopped + total_delivered} Emails",
        horizontalalignment='right',
        verticalalignment='top',
        fontsize=12,
        color='red'
    )

    ''' Totals text (figure-level)
    fig.text(
        0.02, 0.97,
        f"Stopped: {total_stopped}\nDelivered: {total_delivered}",
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=11
    '''

    # Label other necessary titles in the bar graph
    ax.set_ylabel('Number of Emails')
    ax.set_title(f"Email Threats Stopped \n {bottom_date} - {top_date}")    
    plt.show() 

else:
    # Label axis 
    ax = summary.plot.bar(
        x='Type of Threat', 
        y='Stopped', 
        ax=ax,
        rot=0
    )

    # Display total number of emails top right outsifde (fig) of bar graph
    fig.text(
        0.98, 0.97,          
        f"{total_stopped} Emails",
        horizontalalignment='right',
        verticalalignment='top',
        fontsize=12,
        color='red'
    )

    # Display total number of emails center of each bar inside (ax) of the bar graph
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2,  
            height,                         
            str(int(height)),              
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=10
    )
        
    # Label other necessary titles in the bar graph
    ax.set_ylabel('Number of Emails')
    ax.set_title(f"Email Threats Stopped \n {bottom_date} - {top_date}")

    plt.show()
