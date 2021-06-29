from pathlib import Path
import json

from utils.files import get_main_dir


def load_config():
    try:
        base = get_main_dir()
        with open(Path(base, 'config.json'), 'r') as f:
            cfg = json.load(f)
        cfg['db_path'] = Path(base, cfg['database']['path'])
        return cfg
    except json.JSONDecodeError:
        raise
