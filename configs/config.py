import os
from datetime import datetime

from .UNetResLight import Config as UNetResLightConfig
from .UNetResSupervision import Config as UNetResSupervisionConfig


FILE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(FILE_DIR, '../')


def process_config(args):

    if args.CFG_NAME == 'UNetResLight':
        cfg = UNetResLightConfig()
    elif args.CFG_NAME == 'UNetResSupervision':
        cfg = UNetResSupervisionConfig()
    else:
        raise ValueError(f'Unknown CFG_NAME: {args.CFG_NAME}')

    init_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    if args.MODE == 'test' or args.VER_TO_LOAD:
        cfg.COMMON.CHECKPOINT_DIR = os.path.join(ROOT_DIR, f'output/{args.VER_TO_LOAD}')
    else:
        cfg.COMMON.CHECKPOINT_DIR = os.path.join(ROOT_DIR, f'output/{init_time}')

    return cfg
