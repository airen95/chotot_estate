url = 'https://gateway.chotot.com/v1/public/ad-listing?&cg={}&limit=100'

categories = [1010, 1020, 1030, 1040]

tables = {
    'cities': ['id', 'cities_name'],
    'dates': ['id', 'time', 'dates', 'day', 'month', 'year'],
    'district': ['id', 'district_name'],
    'property_info': ['ad_id',
                    'list_time',
                    'category_id,'
                    'account_id',
                    'price',
                    'ward_id',
                    'price_million_per_m2',
                    'longitude',
                    'latitude',
                    'district_id',
                    'cities_id',
                    'subject',
                    'body',
                    'image',
                    'location',
                    'price_string',
                    'sizes',
                    'shop_id'
                    ],
    'shop_profile': ['shop.modifiedDate',
                    'shop_status',
                    'shop_name',
                    'shop_alias',
                    'shop_profile_url',
                    'shop_createdate',
                    'shop_address'
                    ],
    'user_profile': ['id', 'account_name'],
    'wards': ['id', 'ward_name']
}
table_info = {
    'cities': ['region_v2', 'region_name'],
    # 'dates': ['id', 'time', 'dates', 'day', 'month', 'year'],
    'district': ['area_v2', 'area_name'],
    'property_info': ['ad_id',
                    'list_time',
                    'category',
                    'account_id',
                    'price',
                    'ward',
                    'price_million_per_m2',
                    'longitude',
                    'latitude',
                    'area_v2',
                    'region_v2',
                    'subject',
                    'body',
                    'image',
                    'location',
                    'price_string'
                    ],
    'shop_profile': ['modifiedDate',
                    'status',
                    'name',
                    'alias',
                    'profileImageUrl',
                    'createdDate',
                    'address'
                    ],
    'user_profile': ['account_id','account_name'],
    'wards': ['ward','ward_name']
}

# rename = {'category_id': 'category',
#  'district_id': 'area_v2',
#  'cities_id': 'region_v2',
#  'ward_id': 'ward',
#  'shop_alias': 'alias',
#  'shop_status': 'status',
#  'shop_name': 'name',
#  'shop_address': 'address',
#  'shop_profile_url': 'profileImageUrl',
#  'shop_createdate': 'createdDate',
#  'shop.modifiedDate': 'modifiedDate'}