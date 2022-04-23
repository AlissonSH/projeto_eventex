from operator import contains
from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Álisson Sielo Holkem', cpf='12345678901', 
        email='alisson_sielo@hotmail.com', phone='55-99206-7827')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)
        
    def test_subscription_email_from(self):
        expect = 'alisson_sielo@hotmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['alisson_sielo@hotmail.com', 'alisson_sielo@hotmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Álisson Sielo Holkem', 
                    '12345678901', 
                    'alisson_sielo@hotmail.com', 
                    '55-99206-7827']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
