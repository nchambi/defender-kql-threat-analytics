import pandas as pd
import matplotlib.pyplot as plt

# Insert csv file 
filename = input("Enter CSV filename: ")
#timestamp = input("Enter date: ")

df = pd.read_csv(filename)

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

emptyBlocked = (df["DeliveryAction"] == " ")

# Calculate number of emails stopped based on the threat 
Spam = (spam & stopped).sum()
Phish = (phish & stopped).sum()
Phish_spam = (phish_spam & stopped).sum()
Malware = (malware & (stopped | emptyBlocked)).sum()

# Calculate total emails 
totalEmails = Spam + Phish + Phish_spam + Malware

# Print second line of graph title as the date 
timestamp = df["Timestamp"]

# Plot the bar graph
summary = pd.DataFrame({
    'Type of Threat':['Spam', 'Phish', 'Phish, Spam', 'Malware'],
    'Number of Prevented Threats': [Spam, Phish, Phish_spam, Malware]
})

# Determine size of inside (ax) and outside (fig) of bar graph display 
fig, ax = plt.subplots(figsize=(8, 5))

# Label axis 
ax = summary.plot.bar(
    x='Type of Threat', 
    y='Number of Prevented Threats', 
    ax=ax,
    rot=0
)

# Display total number of emails top right outsifde (fig) of bar graph
fig.text(
    0.98, 0.97,          
     f"{totalEmails} Emails",
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
ax.set_ylabel('Number of Prevented Threats')
ax.set_title(f"Email Threats Stopped \n {timestamp}")

plt.show()