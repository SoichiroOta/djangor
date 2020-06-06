from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EntriesConfig(AppConfig):
    name = "djangor.entries"
    verbose_name = _("Entries")

    def ready(self):
        try:
            import djangor.entries.signals  # noqa F401
        except ImportError:
            pass
