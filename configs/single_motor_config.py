single_motor_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['knee'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'knee_group': ['knee']
    },
    'motors': {
        'knee': {
            'orientation': 'direct',
            'type': 'MX-106',
            'id': 1,
            'angle_limit': [-60.0, 60.0],
            'offset': 0.0
        }
    }
}
