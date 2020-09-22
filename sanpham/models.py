from django.db import models

# Create your models here.
class thuonghieu(models.Model):
    ten = models.CharField(max_length=100,default='HATOK',verbose_name='Thương hiệu')

    def __str__(self):
        return self.ten
    class Meta:
        verbose_name_plural = 'Thương hiệu'

# class kho(models.Model):
#     ten = models.CharField(max_length=100,default='HCM',verbose_name='Kho')
#
#     def __str__(self):
#         return self.ten
#     class Meta:
#         verbose_name_plural = 'Kho'

class sanpham(models.Model):
    ten = models.CharField(max_length=200,verbose_name='Tên sản phẩm')
    masp = models.CharField(max_length=100,verbose_name='Mã sản phẩm')
    thuonghieusp = models.ForeignKey(thuonghieu,on_delete=models.CASCADE,verbose_name='Thương hiệu')
    # khosp = models.ForeignKey(kho,on_delete=models.CASCADE,verbose_name='Kho',default='')
    choices = [('cai', 'Cái'), ('hop', 'Hộp'), ('bo', 'Bộ'),('sanpham', 'Sản phẩm')]
    donvi = models.CharField(max_length=25,choices=choices, default='sanpham',verbose_name='Đơn vị')
    giabanle = models.IntegerField(verbose_name='Giá (đã bao gồm VAT)',null=False)
    soluong = models.IntegerField(verbose_name='Tồn kho',default='1')
    hinh = models.ImageField(verbose_name='Hình ảnh',null=False, upload_to='sanpham/',default='media/sanpham/none-img.png')

    def __str__(self):
        return self.ten

    def kovat(self):
        return self.giabanle * 0.9

    class Meta:
        verbose_name_plural = 'Sản phẩm'