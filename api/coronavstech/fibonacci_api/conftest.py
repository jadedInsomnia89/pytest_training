import functools
import pytest
from datetime import datetime, timedelta
from typing import Callable


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta) -> None:
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f'Performance test failed.\nRuntime: {self.runtime.total_seconds()}\nLimit: {self.limit.total_seconds()}'


@pytest.fixture
def time_tracker():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    print(f'\nRuntime: {time_elapsed.total_seconds()}')


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    @functools.wraps(method)
    def run_function_and_validate_runtime(*args, **kwargs):
        start_time = datetime.now()
        result = method(*args, **kwargs)
        end_time = datetime.now()
        runtime = end_time - start_time
        print(f'\nRuntime: {runtime.total_seconds()}')

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
