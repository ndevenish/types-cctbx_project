from typing import Dict

def image_dict_to_unicode(data: Dict) -> Dict:
    """Copy a dict, running .decode() on any bytes keys or values"""
