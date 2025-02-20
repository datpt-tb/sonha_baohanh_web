# -*- coding: utf-8 -*-
{
    'name': "Thông tin bảo hành",
    'summary': "",
    'description': "",
    'author': "",
    'website': "",
    'category': '',
    'version': '0.1',
    'depends': [
        'base', 'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/nguoi_dung.xml',
        'views/province.xml',
        'views/district.xml',
        'views/ward_commune.xml',
        'views/product_type.xml',
        'views/chi_nhanh.xml',
        'views/nhan_vien.xml',
        'views/produce_year_views.xml',
        'views/error_code_views.xml',
        'views/error_group_views.xml',
        'views/form_exchange_views.xml',
        'views/warranty_status_views.xml',
        'views/staff_warranty_information_views.xml',
        'views/warranty_information_views.xml',
        'views/danh_muc.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
