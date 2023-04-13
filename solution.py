import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 734920047 # Ваш chat ID, не меняйте название переменной


def solution(control: np.ndarray, test: np.ndarray) -> bool:
    alpha = 0.05
    _, p_value = ttest_ind(control, test, equal_var = False)
    return p_value < alpha
