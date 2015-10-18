from django.test import TestCase
from .models import Store, MenuItem


class StoreViewTests(TestCase):

    def setUp(self):
        Store.objects.create(name='肯德基', notes='沒有薄皮嫩雞倒一倒算了啦')
        mcdonalds = Store.objects.create(name='McDonalds')
        MenuItem.objects.create(store=mcdonalds, name='大麥克餐', price=99)

    def tearDown(self):
        Store.objects.all().delete()

    def test_list_view(self):
        r = self.client.get('/store/')
        self.assertContains(
            r, '<a class="navbar-brand" href="/">午餐系統</a>',
            html=True,
        )
        self.assertContains(r, '<a href="/store/1/">肯德基</a>', html=True)
        self.assertContains(r, '沒有薄皮嫩雞倒一倒算了啦')
