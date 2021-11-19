from typing import Callable, Dict, List, Tuple

Decorator = Callable


def get_list_of_kwargs_for_function(
        identifiers: str, values: List[Tuple[str,
                                             str]]) -> List[Dict[str, str]]:

    # Parse identifiers and remove whitespace on parsed_identifiers
    parsed_identifiers = identifiers.split(',')

    for i, identifier in enumerate(parsed_identifiers):
        parsed_identifiers[i] = identifier.strip()

    list_of_kwargs_for_function = []

    for tuple_value in values:
        kwargs_for_function = {}

        for i, keyword in enumerate(parsed_identifiers):
            kwargs_for_function[keyword] = tuple_value[i]

        list_of_kwargs_for_function.append(kwargs_for_function)

    print(f'List: {list_of_kwargs_for_function}')
    return list_of_kwargs_for_function


def my_parametrized(identifiers: str, values: List[Tuple[int,
                                                         int]]) -> Decorator:
    def my_parametrized_decorator(function: Callable) -> Callable:
        def run_func_parametrized() -> None:
            list_of_kwargs_for_function = get_list_of_kwargs_for_function(
                identifiers=identifiers, values=values)
            for kwargs_for_function in list_of_kwargs_for_function:
                print(
                    f'Calling function {function.__name__} with {kwargs_for_function}'
                )
                function(**kwargs_for_function)

        return run_func_parametrized

    return my_parametrized_decorator
