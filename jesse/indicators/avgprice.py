from typing import Union

import numpy as np
import talib


def avgprice(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    AVGPRICE - Average Price

    :param candles: np.ndarray
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    res = talib.AVGPRICE(candles[:, 1], candles[:, 3], candles[:, 4], candles[:, 2])

    if sequential:
        return res
    else:
        return None if np.isnan(res[-1]) else res[-1]
