from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


def index(request):
    context = { "name": "Cleyson" }
    html_content = render_to_string('mail/test-mail.html', context)
    plain_content = render_to_string('mail/test-mail.txt', context)
    # mail = EmailMessage(
    #     subject="E-mail de teste",
    #     body="Conteúdo do e-mail",
    #     from_email="no-reply@treinaweb.com.br",
    #     to=["cleyson@mail.com"],
    # )
    # mail.send()
    # send_mail(
    #     subject="E-mail de teste",
    #     message=plain_content,
    #     from_email="no-reply@treinaweb.com.br",
    #     recipient_list=["cleyson@mail.com"],
    #     html_message=html_content
    # )
    mail = EmailMultiAlternatives(
        subject="E-mail de teste",
        body=plain_content,
        from_email="no-reply@treinaweb.com.br",
        to=["cleyson@mail.com"]
    )
    mail.attach_alternative(html_content, "text/html")
    mail.attach_file("mail/midia/anexo.txt")
    mail.send()
    return HttpResponse("E-mail enviado com sucesso")