import numpy as np
import pandas as pd

width, height = 300, 300

attraction_rules = pd.DataFrame(
    {
        "A": {
            "A": -1,
            "B": 1,
            "C": -1
        },
        "B": {
            "A": 1,
            "B": -1,
            "C": 1
        },
        "C": {
            "A": 1,
            "B": 1,
            "C": -1
        }
    }
)