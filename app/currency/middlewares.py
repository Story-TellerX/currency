from django.db.models import F

from currency.models import AnalyticsLog
from currency import choices


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # '''
        # path = "/"
        # method = "GET"
        # AnalitycsLog.objects.filter(request_method=request_method, path=path)
        # '''

        response = self.get_response(request)
        if response:  # if response is existed
            # https://stackoverflow.com/questions/52024039/how-to-use-update-or-create-and-f-to-create-a-new-record-in-django
            request_method = choices.REQUEST_METHOD_CHOICES_MAPPER[request.method]  # get int for request method for DB
            obj, created = AnalyticsLog.objects.get_or_create(
                request_method=request_method, path=request.path, status_code=response.status_code,
                # parameters for filters
                defaults={'counter': 1}
                # default value for record
            )
            if not created:  # if record is not existed
                AnalyticsLog.objects.filter(pk=obj.pk).update(counter=F('counter') + 1)  # counter works inside the DB

        # counter = Analytics.objects.filter(
        #     request_method=request_method, path=request.path).last()
        # if counter:
        #     counter.counter += 1
        #     counter.save()
        # else:
        #     Analytics.objects.create(
        #         request_method=request_method, path=request.path, counter=1)

        return response
