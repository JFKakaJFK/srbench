"""Tests for uDSR sklearn interface."""

import pytest
import numpy as np

from dso import UnifiedDeepSymbolicRegressor, ParallelizedUnifiedDeepSymbolicRegressor
from dso.test.generate_test_data import CONFIG_TRAINING_OVERRIDE


@pytest.fixture
def est():
    return ParallelizedUnifiedDeepSymbolicRegressor()


def test_udsr_regressor(est):
    """Test regression for various configs."""

    # Generate some data
    np.random.seed(0)
    X = np.random.random(size=(10000, 10))
    y = np.random.random(size=(10000,))

    est.fit(X, y, max_time=60)

    print("Best model:", est.expr)


def main():
    my_est = ParallelizedUnifiedDeepSymbolicRegressor()
    test_udsr_regressor(my_est)


if __name__ == "__main__":
    main()
