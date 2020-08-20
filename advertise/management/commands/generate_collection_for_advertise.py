from django.core.management import BaseCommand
from advertise.models import Frontal, InteriorFeature, ExteriorFeature, Locality, Transportation, Landscape, SuitableForDisabled


class Command(BaseCommand):

    def _create_collection(self, model_class, items):
        for item in items:
            model_class.objects.create(name=item)

    def handle(self, *args, **options):
        frontal_values = ["Batı", "Doğu", "Güney", "Kuzey"]

        interior_feature = [
            "ADSL","ADSL-VDSL İnternet", "Fiber İnternet", "Ahşap Doğrama", "Akıllı Ev", "Alarm(Hırsız)",
            "Alarm(Yangın)", "Giysi Odası","Gömme Dolap","Alaturka Tuvalet", "Alüminyum Doğrama",
            "Ankastre Davlumbaz", "Ankastre Buzdolabı", "Ankastre Çamaşır Makinesi", "Ankastre Fırın",
            "Ankastre Bulaşık Makinesi" ,"Beyaz Eşya", "Asansör", "Balkon", "Barbekü","PVC Zemin Kaplama",
            "Laminant Parke Zemin Kaplama", "Üç Boyutlu Zemin Kaplama", "Kauçuk Zemin Kaplama", "Seramik Zemin Kaplama",
            "Mermer Zemin Kaplama", "Lamine Parke", "Masif Parke", "Duşakabin", "Ebeveyn Banyosu", "Jakuzi","Sauna",
            "Fırın", "Giyinme Odası", "Görüntülü Diafon", "Epoksi Zemin Kaplama", "Poliüretan Zemin Kaplama", "Şömine",
            "Amerikan Mutfak", "Tek Duvar Tipi Mutfak", "Ada Tipi mutfak", "Yarım Ada Tipi mutfak",
            "İki taraflı Mutfak", "L tipi Mutfak", "U tipi mutfak", "Taş Duvar","Güç Kaynağı", "Amerikan Kapı",
            "Çelik Kapı", "Ahşap Kapı"
        ]

        exterior_feature = [
            "Asansör", "Buhar Odası", "Güvenlik", "Hamam", "Hidrofor", "Isı Yalıtım", "Jeneratör", "Kablo TV",
            "Kamera Sistemi", "Kapalı Garaj", "Otopark", "Kapıcı", "Kreş",  "Oyun Parkı", "Sauna", "Ses Yalıtımı",
            "Spor Alanı", "Su Deposu", "Tenis Kortu", "Uydu", "Yangın Merdiveni", "Yüzme Havuzu(Açık)",
            "Yüzme Havuzu(Kapalı)", "Isı Yalıtımı", "Ses Yalıtımı"
        ]

        locality = [
            "Alışveriş Merkezi", "Belediye", "Cami",  "Denize Sıfır", "Eczane", "Eğlence Merkezi", "Sinema","Fuar",
            "Havra", "Kilise", "Lise", "Market", "Park", "Polis Merkezi", "Sağlık Ocağı", "Semt Pazarı",
            "Spor Salonu", "Üniversite", "İlkokul-Ortaokul", "İtfaiye", "Şehir Merkezi","Koşu Yolu","Orman","Kaymakalmlık",
            "Valilik", "Karayolları İşletmesi", "Toprak Mahsülleri Ofisi", "Sebze-Meyve Hali", "Ticaret Merkezi",
            "Anaokulu", "Poliklinik", "Kütüphane", "Sağlık Ocağı", "Hastane", "Kafe", "Restaurant", "Balıkçı","Manav",
            "Eczane", "Bakkal", "Market", "Stadyum", "Çay Ocağı", "Kıraathane", "Eğlence Mekanı",
            "Rehabilitasyon Merkezi", "Gündüz Bakım Evi",
        ]

        transportation = [
            "Anayol", "Avrasya Tüneli", "Boğaz Köprüleri", "Cadde", "Deniz Otobüsü", "Dolmuş", "E-5",
            "Havaalanı", "Marmaray", "Metro", "Metrobüs", "Minibüs", "Otobüs Durağı", "Sahil", "TEM",
            "Teleferik", "Tramvay", "Tren İstasyonu", "İskele", "Otogar", "Taksi Durağı", "Deniz Taksi", "Hava Taksi"
        ]

        landscape = ["Boğaz", "Deniz", "Doğa", "Göl", "Havuz", "Park & Yeşil Alan", "Şehir", "Orman", "Akarsu"]

        suitable_for_disabled = [
            "Araç Park Yeri", "Asansör", "Banyo", "Geniş Koridor", "Giriş / Rampa", "Merdiven", "Mutfak", "Oda Kapısı",
            "Park", "Priz / Elektrik Anahtarı", "Tutamak / Korkuluk", "Tuvalet", "Yüzme Havuzu"
        ]

        self._create_collection(Frontal, frontal_values)
        self._create_collection(InteriorFeature, interior_feature)
        self._create_collection(ExteriorFeature, exterior_feature)
        self._create_collection(Locality, locality)
        self._create_collection(Transportation, transportation)
        self._create_collection(Landscape, landscape)
        self._create_collection(SuitableForDisabled, suitable_for_disabled)