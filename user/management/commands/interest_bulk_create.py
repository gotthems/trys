from django.core.management import BaseCommand

from user.models import Interest


class Command(BaseCommand):
    help = "created for bulk operation"

    def _create_collection(self, model_class, items):
        for item in items:
            model_class.objects.create(name=item)

    def handle(self, *args, **options):
        interests_list = ["Aile-Çoçuk", "Alışveriş", "Araba", "Kültür Sanat", "Moda", "Oyun", "Sağlıklı Yaşam",
                          "Seyahat", "Spor", "Teknoloji"]


        self._create_collection(Interest, interests_list)