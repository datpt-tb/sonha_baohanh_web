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
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/nguoi_dung.xml',
        'views/thong_tin_bao_hanh.xml',
        'views/tinh_thanh.xml',
        'views/quan_huyen.xml',
        'views/phuong_xa.xml',
        'views/loai_san_pham.xml',
        'views/chi_nhanh.xml',
        'views/nhan_vien.xml',
        'views/danh_muc.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
