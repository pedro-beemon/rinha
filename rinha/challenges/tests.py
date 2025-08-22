from django.test import TestCase
from .models import Challenge

class ChallengeModelTest(TestCase):
    def test_str(self):
        challenge = Challenge(title="Título Teste")
        self.assertEqual(str(challenge), "Título Teste")
