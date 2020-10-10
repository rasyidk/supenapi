from django.http import JsonResponse


class Response:

    def base(self, values=None, message="", status=200):
        if values is None:
            values = []

        return JsonResponse({
            'values': values,
            'message': message
        }, status=status)

    def pages(self, values=None, message="",totaldata="" ,status=200):
        if values is None:
            values = []

        return JsonResponse({
            'values': values,
            'pages': message,
            'totaldata':totaldata
        }, status=status)


    @staticmethod
    def ok(values=None, message=""):
        return Response().base(values=values, message=message, status=200)


    @staticmethod
    def paginate(values=None, message="",totaldata=""):
        return Response().pages(values=values, message=message, totaldata=totaldata, status=200)

    @staticmethod
    def badRequest(values=None, message=""):
        return Response().base(values=values, message=message, status=400)

# class ResponsePaginate:
    
#     def base(self, values=None, pages="", status=200):
#         if values is None:
#             values = []

#         return JsonResponse({
#             'values': values,
#             'pages': pages
#         }, status=status)
    

#     @staticmethod
#     def ok(values=None, pages=""):
#         return Response().base(values=values, pages=message, status=200)

#     @staticmethod
#     def badRequest(values=None, pages=""):
#         return Response().base(values=values, pages=message, status=400)