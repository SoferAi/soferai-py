# content of conftest.py


import pytest
from pytest import CallInfo, Item

# store history of failures per test class name and per index in parametrize (if parametrize used)
_test_failed_incremental: dict[str, dict[tuple[int, ...], str]] = {}


def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> None:
    if "incremental" in item.keywords and call.excinfo is not None:
        # the test has failed
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # retrieve the index of the test (if parametrize is used in combination with incremental)
        parametrize_index = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
        # retrieve the name of the test function
        test_name = item.originalname or item.name
        # store in _test_failed_incremental the original name of the failed test
        _test_failed_incremental.setdefault(cls_name, {}).setdefault(parametrize_index, test_name)


def pytest_runtest_setup(item: Item) -> None:
    if "incremental" in item.keywords:
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # check if a previous test has failed for this class
        if cls_name in _test_failed_incremental:
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            # retrieve the name of the first test function to fail for this class name and index
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            # if name found, test has failed for the combination of class name & test name
            if test_name is not None:
                pytest.xfail(f"previous test failed ({test_name})")
