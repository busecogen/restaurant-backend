from django.core.management import BaseCommand

from ranger.models import Menu
from restaurant_backend.menu import menu_data


class Command(BaseCommand):
    help = "Fetch menu list into database of Menu model"

    def handle(self, *args, **options):
        # Menu.objects.all().delete()
        self.visit_menu(menu_data, None)

    def visit_menu(self, menu_list, parent: Menu or None):
        for item in menu_list:
            menu, created = Menu.objects.get_or_create(
                name=item.get('name'),
                url=item.get('url'),
                parent=parent
            )
            if len(item.get('submenu')) > 0:
                self.visit_menu(item.get('submenu'), menu)
