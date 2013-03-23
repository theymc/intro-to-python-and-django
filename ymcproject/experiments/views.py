from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView


# This is a function based view
def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# This is a class based view, using a generic view provided by django
class TimeView(TemplateView):
    template_name = "time.html"

    def get_context_data(self, *args, **kwargs):
        now = datetime.datetime.now()
        return {'current_date': now}
