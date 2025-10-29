from django.test import TestCase
from django.conf import settings


class SettingsSmokeTest(TestCase):
    def test_database_name_set(self):
        # Basic sanity check: database name is configured (dev/default value)
        self.assertIn("default", settings.DATABASES)
        self.assertTrue(settings.DATABASES["default"].get("NAME"))
