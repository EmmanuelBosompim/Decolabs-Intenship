message = input("Paste the message text to analyze: ")

suspicious_keywords = [
    "urgent",
    "immediately",
    "verify",
    "password",
    "mfa",
    "payment",
    "account suspended",
    "click here",
    "qr code",
    "wire transfer",
    "confidential"
]

print("\nPHISHING AWARENESS TRIAGE")
print("-------------------------")

found = []

for keyword in suspicious_keywords:
    if keyword.lower() in message.lower():
        found.append(keyword)
        print("[!] Suspicious indicator:", keyword)

if not found:
    print("[!] No listed keywords were found.")

print("\nReminder:")
print("Keyword detection alone does not prove phishing.")
print("Pause, verify independently, and report when appropriate.")
