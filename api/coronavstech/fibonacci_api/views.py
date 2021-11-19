from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.coronavstech.fibonacci_api.fibonacci.dynamic import fibonacci_dynamic_v2


@api_view(http_method_names=['GET'])
def index(request: Request):
    '''
        calculates fibonacci number from given input
        input:
            n
    '''
    # Validate the data
    try:
        n = int(request.GET.get('n'))

        if n < 0:
            raise ValueError

    except ValueError:
        return Response(
            {
                'status': 'Error. Must send an integer 0 or greater',
                'value': request.GET.get('n')
            },
            status=400)

    # Calculate fibonacci number
    fib_num = fibonacci_dynamic_v2(n=n)
    fib_num = str(fib_num)

    return Response(
        {
            'status': 'successfully calculated fibonacci number',
            'value': fib_num
        },
        status=200)
