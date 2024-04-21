simCLR_params = {
    'cleaner': 'linear',
    'produce_features': ['norm_xyz', 'jerk'],
    'filter': None,
    'filter_window': 3,
    'rescaler': None,
    'split_type': 'loso',
    'hold_out': 3,
    'duration': 2,
    'stride': 1,
    'selection_method': 'in total',
    'tolerance': 0.3,
    'use_features': ['acc_x', 'acc_y', 'acc_z', 'norm_xyz', 'jerk'],
    'augmentations': ['shift'],
    'common_augmentations': None,
    'shift_pad': 1,
    'batch_method': 'random',
    'batch_size': 128,
    'ssl_model': 'simCLR',
    'encoder': 'Attention',
    'cnn_blocks': 4,
    'clr_temperature': 0.05,
    'optimizer': 'adam',
    'epochs': 150,
    'decay_steps': 0,
    'lr_decay': None,
    'learning_rate': 0.0001,
    'attach_head': True,
    'negative_dataset': 'same',
    'negative_subject': 'same',
    'negative_activity': 'same',
    'negative_position': 'all'
}