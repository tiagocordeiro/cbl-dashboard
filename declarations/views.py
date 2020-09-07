import ssl

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa

from declarations.facade import link_callback


@login_required
def declarations_list(request):
    return render(request, 'declarations/list.html')


@login_required
def declaration_detail(request):
    return render(request, 'declarations/detail.html')


@login_required
def declaration_pdf_gen(request):
    ssl._create_default_https_context = ssl._create_unverified_context

    template_path = 'declarations/pdfgen.html'
    context = {'parceiro': "parceiro",
               'usuario': "usuario",
               'pedido': "pedido",
               'pedido_itens': "pedido_itens",
               'pedido_total': "pedido_total",
               'pedido_itens_qt': "pedido_itens_qt"}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf;charset=utf-8')
    response[
        'Content-Disposition'] = f'attachment; filename="Declaracao-numero.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf8',
                                 link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
