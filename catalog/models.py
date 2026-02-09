from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="اسم التصنيف"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="الرابط المختصر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="اسم المنتج"
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name="صورة المنتج"
    )
    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="الكمية"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
