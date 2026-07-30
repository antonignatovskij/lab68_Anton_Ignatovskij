import json

from django.http.response import JsonResponse
from django.views.generic.base import View


# Create your views here.

class CalculateView(View):
    def post(self, request, *args, **kwargs):
        if request.body:
            body = json.loads(request.body)
            if 'add' in request.path.split('/'):
                answer = self.add_number(body)
            elif 'subtract' in request.path.split('/'):
                answer = self.subtract(body)
            elif 'multiply' in request.path.split('/'):
                answer = self.multiply(body)
            elif 'divide' in request.path.split('/'):
                answer = self.divide(body)
            else:
                answer = {"error": 'wrong path'}
        else:
            answer = {"error": "nothing"}

        if 'error' in answer:
            return JsonResponse(answer, status=400)
        return JsonResponse(answer)


    def add_number(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return {"answer": body['a'] + body['b']}
            except TypeError:
                return {"error": 'concatenate str is impossible'}
        else:
            return {"error": "No 'a' or 'b' in your body keys"}

    def subtract(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return {"answer": body['a'] - body['b']}
            except TypeError:
                return {"error": 'subtract str is impossible'}
        else:
            return {"error": "No 'a' or 'b' in your body keys"}

    def multiply(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return {"answer": body['a'] * body['b']}
            except TypeError:
                return {"error": 'multiply str is impossible'}
        else:
            return {"error": "No 'a' or 'b' in your body keys"}

    def divide(self, body):
        required_keys = ["a", "b"]
        if all(key in body for key in required_keys):
            try:
                return {"answer": body['a'] / body['b']}
            except TypeError:
                return {"error": 'divide str is impossible'}
            except ZeroDivisionError:
                return {"error": "division by zero"}
        else:
            return {"error": "No 'a' or 'b' in your body keys"}

