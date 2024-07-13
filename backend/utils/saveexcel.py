import os
from typing import Dict

import pandas as pd


def save_excel(name: str, informations: Dict):
    excel_path = os.path.join('backend/data', name)
    df = pd.DataFrame(informations)
    df.to_excel(excel_path, index=False, engine='openpyxl')
