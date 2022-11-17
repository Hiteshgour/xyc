from django.shortcuts import render
from .models import Member
from .utils import get_tenant
# Create your views here.

def out_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)
    return render(request, 'our_team.html', {'tenant':tenant, 'members': members})