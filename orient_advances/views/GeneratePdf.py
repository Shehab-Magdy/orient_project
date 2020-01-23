from django.http import HttpResponse
from django.views.generic import View
# from django.template.loader import get_template
from orient_advances.models import utils
from orient_advances.models.advance import Advance
import pyarabic.number

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # an = pyarabic.number.ArNumbers()
        user_full_name = request.user.username
        user_id = request.user.id
        sec = request.user.section
        adv = Advance.objects.filter(emplyee_id=user_id).order_by("-id")[0]
        # am = str(adv.amount)
        # ar_no = an.int2str(am)
        # print (an.int2str(am))
        context = {
            'date': adv.request_date, 
            'amount': adv,
            'employee_name': user_full_name,
            'section': sec,
            'order_id': adv.id,
            # 'ar_no': ar_no,
        }
        pdf = utils.render_to_pdf('orient_advances/reports/advance_report.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Advance Request No.%s for %s.pdf' %(adv.id,user_full_name)
            content = "inline; filename='%s'" %(filename)
            response['Content-disposition']= content
            return response
        return HttpResponse("Not Found")