from django.db import models
from jalali_date import datetime2jalali

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم')

    def __str__(self):
        return self.name


class ProductSold(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, verbose_name="کالا")
    count = models.IntegerField(verbose_name="تعداد")
    sell_date_time = models.DateTimeField(verbose_name="زمان فروش")
    monthdict = {
        'Farvardin': 'فروردین',
        'Ordibehesht': 'اردیبهشت',
        'Khordad': 'خرداد',
        'Tir': 'تیر',
        'Mordad': 'مرداد',
        'Shahrivar': 'شهریور',
        'Mehr': 'مهر',
        'Aban': 'آبان',
        'Azar': 'آذر',
        'Dey': 'دی',
        'Bahman': 'بهمن',
        'Esfand': 'اسفند',
    }

    def __str__(self):
        return f"{self.product.name} - {self.count} فروخته شده در {self.sell_date_time}"
    def get_month_jalali(self):
        jalali_month = datetime2jalali(self.sell_date_time).strftime('%B')
        return self.monthdict.get(jalali_month, jalali_month)
    def get_report(self):
        products = Product.objects.all()
        result = {}
        for month in self.monthdict.values():
            result[month] = [0] * products.count()
        for index, product in enumerate(products):
            products_sold = ProductSold.objects.filter(product_id=product.id)

            for ps in products_sold:
                month = ps.get_month_jalali()
                count = ps.count
                result[month][index] += count

        return result
