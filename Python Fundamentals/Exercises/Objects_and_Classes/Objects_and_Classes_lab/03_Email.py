class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while command != 'Stop':
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))
for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())