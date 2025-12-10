import pandas as pd
import matplotlib.pyplot as plt

filename = input("Enter CSV filename: ")
timestamp = input("Enter date: ")

df = pd.read_csv(filename)

spam = df["ThreatTypes"] == "Spam"
phish = df["ThreatTypes"] == "Phish"
phish_spam = df["ThreatTypes"] == "Phish, Spam"
malware = df["ThreatTypes"] == "Malware"

stopped = (
    (df["DeliveryAction"] == "Junked") |
    (df["DeliveryAction"] == "Quarantined") |
    (df["DeliveryAction"] == "Blocked"))

emptyBlocked = (df["DeliveryAction"] == " ")

Spam = (spam & stopped).sum()
Phish = (phish & stopped).sum()
Phish_spam = (phish_spam & stopped).sum()
Malware = (malware & (stopped | emptyBlocked)).sum()

totalEmails = Spam + Phish + Phish_spam + Malware

summary = pd.DataFrame({
    'Type of Threat':['Spam', 'Phish', 'Phish, Spam', 'Malware'],
    'Number of Prevented Threats': [Spam, Phish, Phish_spam, Malware]
})

fig, ax = plt.subplots(figsize=(8, 5))

ax = summary.plot.bar(
    x='Type of Threat', 
    y='Number of Prevented Threats', 
    ax=ax,
    rot=0
)

fig.text(
    0.98, 0.97,          
     f"{totalEmails} Emails",
    horizontalalignment='right',
    verticalalignment='top',
    fontsize=12,
    color='red'
)

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

ax.set_ylabel('Number of Prevented Threats')
ax.set_title(f"Email Threats Stopped \n {timestamp}")

plt.show()