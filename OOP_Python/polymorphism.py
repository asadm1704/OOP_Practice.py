'''Create a media player that can play different file types polymorphically:

Create base class MediaFile with:

play() method (returns "Playing media...")

get_duration() method

Create subclasses:

MP3File: Override play() to return "Playing MP3: [song details]"

MP4File: Override play() to return "Playing MP4: [video details]"

WAVFile: Override play() to return "Playing WAV: [audio details]"

Create a MediaPlayer class with:

add_file(file) method

play_all() method that plays all files polymorphically'''
class MediaFile:
    def play(self):
        return "Playing media..."
    
    def get_duration(self):
        pass
class MP3File(MediaFile):
    def __init__(self, filename, song_details, duration):
        self.filename = filename
        self.song_details = song_details
        self.duration = duration

    def play(self):
        return f"Playing MP3: {self.song_details} ({self.duration}s)"
    
    def get_duration(self):
        return self.duration


class MP4File(MediaFile):
    def __init__(self, filename, video_details, duration):
        self.filename = filename
        self.video_details = video_details
        self.duration = duration

    def play(self):
        return f"Playing MP4: {self.video_details} ({self.duration}s)"
    
    def get_duration(self):
        return self.duration


class WAVFile(MediaFile):
    def __init__(self, filename, audio_details, duration):
        self.filename = filename
        self.audio_details = audio_details
        self.duration = duration

    def play(self):
        return f"Playing WAV: {self.audio_details} ({self.duration}s)"
    
    def get_duration(self):
        return self.duration
class MediaPlayer:
    def __init__(self):
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def play_all(self):
        for file in self.files:
            print(file.play())
# Example usage
# Expected output:
player = MediaPlayer()
player.add_file(MP3File("song.mp3", "Artist - Title", 180))
player.add_file(MP4File("video.mp4", "My Vacation", 300))
player.add_file(WAVFile("sound.wav", "Sound Effect", 5))

player.play_all()
# Playing MP3: Artist - Title (180s)
# Playing MP4: My Vacation (300s)  
# Playing WAV: Sound Effect (5s)w


'''Create a payment system that calculates salaries differently for different employees:

Base class Employee with:

calculate_salary() method

get_details() method

Subclasses with different salary calculations:

HourlyEmployee: salary = hours_worked × hourly_rate

SalariedEmployee: salary = monthly_salary + bonus

CommissionEmployee: salary = base_salary + (sales × commission_rate)

Create a Payroll class that can process all employees polymorphically.'''
class Employee:
    def calculate_salary(self):
        pass

    def get_details(self):
        pass                
class HourlyEmployee(Employee): 
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def get_details(self):
        return f"Hourly Employee: {self.name}, Hours Worked: {self.hours_worked}, Hourly Rate: {self.hourly_rate}"
class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus):
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus

    def get_details(self):
        return f"Salaried Employee: {self.name}, Monthly Salary: {self.monthly_salary}, Bonus: {self.bonus}"
class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, sales, commission_rate):
        self.name = name
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_salary(self):
        return self.base_salary + (self.sales * self.commission_rate)

    def get_details(self):
        return f"Commission Employee: {self.name}, Base Salary: {self.base_salary}, Sales: {self.sales}, Commission Rate: {self.commission_rate}"
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        for employee in self.employees:
            print(f"{employee.get_details()} - Salary: {employee.calculate_salary()}")


# Expected output:
payroll = Payroll()
payroll.add_employee(HourlyEmployee("Alice", 40, 20))  # 40 hrs × $20
payroll.add_employee(SalariedEmployee("Bob", 5000, 1000))  # $5000 + $1000 bonus
payroll.add_employee(CommissionEmployee("Charlie", 3000, 50000, 0.1))  # $3000 + 10% of $50000

payroll.process_payroll()
# Alice: $800.00
# Bob: $6000.00  
# Charlie: $8000.00 
'''Exercise 3: Notification System
Create a notification system that sends messages through different channels:

Base class Notification with:

send(message) method

get_status() method

Subclasses for different channels:

EmailNotification: sends via email

SMSNotification: sends via SMS

PushNotification: sends push notification

SlackNotification: sends to Slack channel

Create a NotificationManager that can send notifications through all channels.'''
class Notification:
    def send(self, message):
        pass

    def get_status(self):
        pass
class EmailNotification(Notification):
    def __init__(self, email_address):
        self.email_address = email_address
        self.status = "Not Sent"

    def send(self, message):
        # Simulate sending email
        print(f"Sending Email to {self.email_address}: {message}")
        self.status = "Sent"

    def get_status(self):
        return self.status
class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.status = "Not Sent"

    def send(self, message):
        # Simulate sending SMS
        print(f"Sending SMS to {self.phone_number}: {message}")
        self.status = "Sent"

    def get_status(self):
        return self.status
class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "Not Sent"

    def send(self, message):
        # Simulate sending push notification
        print(f"Sending Push Notification to {self.device_id}: {message}")
        self.status = "Sent"

    def get_status(self):
        return self.status
class SlackNotification(Notification):
    def __init__(self, channel):
        self.channel = channel
        self.status = "Not Sent"

    def send(self, message):
        # Simulate sending Slack message
        print(f"Sending Slack message to {self.channel}: {message}")
        self.status = "Sent"

    def get_status(self):
        return self.status

class NotificationManager:
    def __init__(self):
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

    def send_all(self, message):
        for notification in self.notifications:
            notification.send(message)
            print(f"Status: {notification.get_status()}")

# Expected output:
manager = NotificationManager()
manager.add_notification(EmailNotification("user@example.com"))
manager.add_notification(SMSNotification("+1234567890"))
manager.add_notification(PushNotification("device_token_123"))
manager.add_notification(SlackNotification("#general"))

manager.send_all("Server is down!")
# Sending email to user@example.com: Server is down!
# Sending SMS to +1234567890: Server is down!
# Sending push to device_token_123: Server is down!
# Sending to Slack #general: Server is down!