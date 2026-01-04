import collections
import numpy as np
import pandas as pd
import re

from argparse import Namespace

args = Namespace(
    raw_dataset_csv="data/surnames/surnames.csv",
    train_proportion=0.7,
    val_proportion=0.15,
    test_proportion=0.15,
    output_munged_csv="data/surnames/surnames_with_splits.csv",
    seed=1337
)