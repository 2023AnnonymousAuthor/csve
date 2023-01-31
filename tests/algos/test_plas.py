import pytest

from d3rlpy.algos.plas import PLAS, PLASWithPerturbation
from tests import performance_test

from .algo_test import algo_pendulum_tester, algo_tester, algo_update_tester


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
@pytest.mark.parametrize(
    "scalers", [(None, None, None), ("min_max", "min_max", "min_max")]
)
def test_plas(
    observation_shape,
    action_size,
    q_func_factory,
    scalers,
):
    scaler, action_scaler, reward_scaler = scalers
    plas = PLAS(
        q_func_factory=q_func_factory,
        scaler=scaler,
        action_scaler=action_scaler,
        reward_scaler=reward_scaler,
        warmup_steps=0,
    )
    algo_tester(
        plas,
        observation_shape,
        test_policy_copy=True,
        test_q_function_copy=True,
    )
    algo_update_tester(
        plas,
        observation_shape,
        action_size,
        test_policy_optim_copy=True,
        test_q_function_optim_copy=True,
    )


@performance_test
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
def test_plas_performance(q_func_factory):
    plas = PLAS(q_func_factory=q_func_factory)
    algo_pendulum_tester(plas, n_trials=1)


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("action_size", [2])
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
@pytest.mark.parametrize(
    "scalers", [(None, None, None), ("min_max", "min_max", "min_max")]
)
def test_plas_with_perturbation(
    observation_shape,
    action_size,
    q_func_factory,
    scalers,
):
    scaler, action_scaler, reward_scaler = scalers
    plas = PLASWithPerturbation(
        q_func_factory=q_func_factory,
        scaler=scaler,
        action_scaler=action_scaler,
        reward_scaler=reward_scaler,
        warmup_steps=0,
    )
    algo_tester(
        plas,
        observation_shape,
        test_policy_copy=True,
        test_q_function_copy=True,
    )
    algo_update_tester(
        plas,
        observation_shape,
        action_size,
        test_policy_optim_copy=True,
        test_q_function_optim_copy=True,
    )


@performance_test
@pytest.mark.parametrize("q_func_factory", ["mean", "qr", "iqn", "fqf"])
def test_plas_with_perturbation_performance(q_func_factory):
    plas = PLASWithPerturbation(q_func_factory=q_func_factory)
    algo_pendulum_tester(plas, n_trials=1)
