from django.http import HttpResponse


def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(ahora)

