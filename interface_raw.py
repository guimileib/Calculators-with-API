from abc import ABC, abstractmethod

class NotificationSender(ABC): # classe abstrata NotificationSender que herda de ABC

    @abstractmethod # decorator de um método
    def send_notification(self, message: str) -> None:
        pass     

class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'Email message: {message}')

class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'SMS message: {message}')

class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message) # o método __notification_sender é um tipo NotificationSender

obj = Notificator(SMSNotificationSender())
obj.send("Hello World")

'''obj1 = SMSNotificationSender()
obj1.send_notification("SMS Notification")
obj2 = EmailNotificationSender()
obj2.send_notification("Email Notification")'''

        