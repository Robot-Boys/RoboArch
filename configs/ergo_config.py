ergo_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['base', 'head'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'base': ['base_pan'],
        'head': ['head_pan']
    },
    'motors': {
        'base_pan': {
            'orientation': 'direct',
            'type': 'MX-28',
            'id': 2,
            'angle_limit': [-90.0, 90.0],
            'offset': 0.0
        },
        'head_pan': {
            'orientation': 'indirect',
            'type': 'MX-28',
            'id': 1,
            'angle_limit': [-90.0, 90.0],
            'offset': 0.0
        }
    }
}
