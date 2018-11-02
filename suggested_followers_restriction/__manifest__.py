# -*- coding: utf-8 -*-
#
# Copyright 2018 Roman Egunkov <romanegunkov@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    'name': "Allow or deny to suggest followers",

    'summary': """
        Allow or deny to suggest add parthers as recipient and follower""",

    'description': """
        Allow or deny to suggest add parthers as recipient and follower.
                        
        Unchecked suggested partners by default.
    """,

    'author': "Roman Egunkov",
    'website': "https://github.com/romanegunkov/odoo-addons/suggested_followers_restriction",
    'license': "LGPL-3",

    'category': 'Discuss',
    'version': '0.1-dev',

    'depends': ['base', 'mail'],

    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],    
    'demo': [],
    'qweb': [
        'static/src/xml/chatter.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
