head_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['up_down', 'left_right', 'rotation'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'head': ['up_down', 'left_right', 'rotation']
    },
    'motors': {
        'up_down': {
            'orientation': 'direct',
            'type': 'MX-28',
            'id': 2,
            'angle_limit': [-60, 60.0],
            'offset': 0.0
        },
        'left_right': {
            'orientation': 'direct',
            'type': 'MX-28',
            'id': 1,
            'angle_limit': [-60.0, 60.0],
            'offset': 0.0,

        },
        'rotation': {
            'orientation': 'direct',
            'type': 'MX-28',
            'id': 3,
            'angle_limit': [-60.0, 60.0],
            'offset': 0.0
        }
    }
}
