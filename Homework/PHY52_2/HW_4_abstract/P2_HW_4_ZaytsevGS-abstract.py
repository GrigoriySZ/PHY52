import random
import re
from abc import ABC, abstractmethod


class Notification(ABC):
    """Абстрактный базовый класс уведомления.

    Methods:
        send()
            Отправляет уведомление пользователю
        get_details()
            Возвращает детали уведомления
        retry()
            Повторно отправляет уведомление при неудачной отправке

    """

    STATUS = {
        'pending': 'Ожидает отправку',
        'sent': 'Отправлено',
        'failed': 'Ошибка отправки'
    }

    def __init__(self, message: str):
        """Инициализирует класс с начальными полями

        Parameters:
            message (str): Содержание уведомления

        """

        self.message = self._validate_message(message)
        self.status = self.STATUS['pending']

    def _validate_message(self, message: str):
        """Проверяет наличие содержимого в строке сообщения"""
        if not isinstance(message, str):
            raise TypeError
        elif not message.strip():
            raise ValueError
        return message

    @abstractmethod
    def send(self):
        """Отправляет уведомление пользователю"""
        pass

    @abstractmethod
    def get_details(self):
        """Возвращает детали уведомления"""
        pass

    @abstractmethod
    def retry(self):
        """Повторно отправляет уведомление при неудачной отправке"""
        pass

class EmailNotification(Notification):
    """Класс уведомления по электронной почте.

    Methods:
        send():
            Отправляет уведомление пользователю
        get_details():
            Возвращает детали уведомления
        retry():
            Повторно отправляет уведомление при неудачной отправке

    """
    def __init__(self, recipient: str, message: str):
        super().__init__(message)
        self.recipient = self._validate_email_recipient(recipient)
        self.notification_type = 'Email'

    def _validate_email_recipient(self, recipient: str):
        """Проверяет правильность email адреса получателя"""
        pattern = r'[\w\.-]+@[\w\.-]+\.[\w+]'
        if not isinstance(recipient, str):
            raise TypeError
        elif not re.search(pattern, recipient):
            raise ValueError
        return recipient

    def send(self):
        """Отправляет уведомление пользователю на электронную почту"""
        print(f'Отправка уведомления на EMAIL {self.recipient}...')
        success = random.choice([True, False, True, True, False])
        if success:
            self.status = self.STATUS['sent']
        else:
            self.status = self.STATUS['failed']

    def get_details(self):
        """Возвращает детали Email уведомления"""
        details = {
            'notification_type': self.notification_type,
            'recipient': self.recipient,
            'message': self.message,
            'status': self.status
        }
        return details

    def retry(self):
        """Повторное отправляет Email уведомление, если уведомление не доставлено"""
        if self.status == self.STATUS['failed']:
            print('Повторная отправка...')
            self.send()
        else:
            print('Уведомление доставлено!')

class SMSNotification(Notification):
    """Класс уведомления по SMS.

        Methods:
            send():
                Отправляет уведомление пользователю
            get_details():
                Возвращает детали уведомления
            retry():
                Повторно отправляет уведомление при неудачной отправке

        """

    def __init__(self, recipient: str, message: str):
        super().__init__(recipient, message)
        self.recipient = self._validate_sms_recipient(recipient)
        self.notification_type = 'SMS'

    def _validate_sms_recipient(self, recipient: str):
        """Проверяет правильность номера получателя"""
        pattern = r'\+?\d[\d\s\-()]{10,15}'
        if not isinstance(recipient, str):
            raise TypeError
        elif not re.search(pattern, recipient):
            raise ValueError
        return recipient

    def send(self):
        """Отправляет SMS уведомление пользователю"""
        print(f'Отправка SMS уведомления {self.recipient}...')
        success = random.choice([True, False, True, True, False])
        if success:
            self.status = self.STATUS['sent']
        else:
            self.status = self.STATUS['failed']

    def get_details(self):
        """Возвращает детали SMS уведомления

        Returns:
            dict: Словарь с деталями уведомления

        """
        details = {
            'notification_type': self.notification_type,
            'recipient': self.recipient,
            'message': self.message,
            'status': self.status
        }
        return details

    def retry(self):
        """Повторное отправляет SMS уведомление, если уведомление не доставлено"""
        if self.status == self.STATUS['failed']:
            print('Повторная отправка...')
            self.send()
        else:
            print('Уведомление доставлено!')

class NotificationManager:
    """Класс для управления отправки уведомлений через различные каналы."""

    def __init__(self):
        """Инициализируем менеджер уведомлений"""
        self.notifications = []

    def add_notification(self, notification: Notification):
        """Добавляет уведомление в очередь отправки

        Parameters:
            notification (Notification): Объект уведомления

        """
        self.notifications.append(notification)

    def send_notifications(self):
        """Отправляет все добавленные уведомления"""
        for notification in self.notifications:
            notification.send()

    def show_statuses(self):
        """Выводит на терминал статус отправки уведомлений"""
        for notif in self.notifications:
            print(f'Type: {notif.notification_type}; '
                  f'Recipient: {notif.recipient}; '
                  f'Message: {notif.message}; '
                  f'Status: {notif.status}.')

# Запускаем менеджер
if __name__ == '__main__':
    manager = NotificationManager()

    # Создаем объекты класса уведомления
    email_1 = EmailNotification('user_1@google.com', 'Ваше уведомление от Google...')
    email_2 = EmailNotification('user_2@yandex.ru', 'Ваше уведомление от Yandex...')
    sms_1 = SMSNotification('+79931535577', 'Уведомляем вас о...')
    sms_2 = SMSNotification('+76482146685', 'Спешим Вам напомнить о...')

    notifications = [email_1, email_2, sms_1, sms_2]

    # Добавляем объекты уведомлений в очередь на отправку
    for notif in notifications:
        manager.add_notification(notif)

    # Отправляем все уведомления
    manager.send_notifications()

    # Проверяем уведомления
    manager.show_statuses()

    # Повторяем отправку для уведомлений с ошибкой
    for notif in notifications:
        if notif.status == notif.STATUS['failed']:
            notif.retry()

    manager.show_statuses()