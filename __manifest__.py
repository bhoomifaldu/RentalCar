# -*- coding: utf-8 -*-
{
    'name': 'Rental Car',
    'version': '1.0',
    'category': 'Product',
    'author' : 'Bhoomi Patel',
    'sequence': 60,
    'summary': 'Vehical Master',
    'description': """Vehical Master""",
    'depends': ['base'],
    'data': [
            'views/vehical_master.xml',
            'views/trip_information.xml',
            'data/ir_sequence_data.xml',
            # 'security/ir.model.access.csv',
	],

    'installable': True,
    'auto_install': False,
}