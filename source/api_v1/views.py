import json

from django.http.response import JsonResponse
from django.views.generic.base import View


# Create your views here.

class CalculateView(View):
    def get(self, request, *args, **kwargs):
        if request.body:
            body = json.loads(request.body)
            if 'add' in request.path.split('/'):
                answer = {"answer": self.add_number(body)}
            elif 'subtract' in request.path.split('/'):
                answer = {"answer": self.subtract(body)}
            elif 'multiply' in request.path.split('/'):
                answer = {"answer": self.multiply(body)}
            elif 'divide' in request.path.split('/'):
                answer = {"answer": self.divide(body)}
            else:
                answer = {"answer": 'wrong path'}
        else:
            answer = {"answer": "nothing"}
        return JsonResponse(answer)


    def add_number(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return body['a'] + body['b']
            except TypeError:
                return 'concatenate str is impossible'
        else:
            return "No 'a' or 'b' in your body keys"

    def subtract(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return body['a'] - body['b']
            except TypeError:
                return 'suptract str is impossible'
        else:
            return "No 'a' or 'b' in your body keys"

    def multiply(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return body['a'] * body['b']
            except TypeError:
                return 'multiply str is impossible'
        else:
            return "No 'a' or 'b' in your body keys"

    def divide(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return body['a'] / body['b']
            except TypeError:
                return 'divide str is impossible'
            except ZeroDivisionError:
                return "division by zero"
        else:
            return "No 'a' or 'b' in your body keys"

