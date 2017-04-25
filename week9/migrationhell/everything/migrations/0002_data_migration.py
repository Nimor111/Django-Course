# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 18:11
from __future__ import unicode_literals

from django.db import migrations


def f(apps, schema_editor):
    RealUser = apps.get_model('users', 'User')
    OldUser = apps.get_model('everything', 'User')

    RealCategory = apps.get_model('products', 'Category')
    OldCategory = apps.get_model('everything', 'Category')

    RealProduct = apps.get_model('products', 'Product')
    OldProduct = apps.get_model('everything', 'Product')

    RealComment = apps.get_model('comments', 'Comment')
    OldComment = apps.get_model('everything', 'Comment')

    RealOrder = apps.get_model('cart', 'Order')
    OldOrder = apps.get_model('everything', 'Order')

    RealInvoice = apps.get_model('cart', 'Invoice')
    OldInvoice = apps.get_model('everything', 'Invoice')

    for user in OldUser.objects.all():
        RealUser.objects.create(uuid=user.uuid, email=user.email)

    for category in OldCategory.objects.all():
        RealCategory.objects.create(id=category.id,
                                    name=category.name)

    for product in OldProduct.objects.all():
        new_product = RealProduct.objects.create(uuid=product.uuid,
                                                 name=product.name)

        for p in product.categories.all():
            for c in product.categories.all():
                new_c = RealCategory.objects.get(id=c.id)
                new_product.categories.add(new_c)

    for comment in OldComment.objects.all():
        user = RealUser.objects.get(uuid=comment.user.uuid)
        product = RealProduct.objects.get(uuid=comment.product.uuid)
        RealComment.objects.create(id=comment.id,
                                   user=user,
                                   product=product,
                                   text=comment.text)

    for order in OldOrder.objects.all():
        user = RealUser.objects.get(uuid=order.user.uuid)
        new_order = RealOrder.objects.create(uuid=order.uuid,
                                             user=user)

        for p in order.products.all():
            new_p = RealProduct.objects.get(uuid=p.uuid)
            new_order.products.add(new_p)

    for invoice in OldInvoice.objects.all():
        order = RealOrder.objects.get(uuid=invoice.order.uuid)
        new_invoice = RealInvoice.objects.create(id=invoice.id,
                                                 company_data=invoice.company_data,
                                                 order=order,
                                                 total=invoice.total)


class Migration(migrations.Migration):

    dependencies = [
        ('everything', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(f)
    ]
