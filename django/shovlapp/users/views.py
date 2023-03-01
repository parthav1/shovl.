from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

from dotenv import load_dotenv
load_dotenv()
import os
import supabase
from supabase import create_client, Client # type: ignore

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = supabase.create_client(url, key) # type: ignore

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    watchlist_vendors = supabase.table('shovl_watchlist').select("*").execute()
    context = {
        'watchlist_venders': watchlist_vendors.data,
    }
    return render(request, 'users/profile.html', context)