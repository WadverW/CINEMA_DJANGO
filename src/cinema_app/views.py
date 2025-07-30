from django.shortcuts import render


def main(request):
    return render(request, "cinema_app/main_page.html")


def lte_admin(request):
    return render(request, "adminlte/lte_admin.html")
