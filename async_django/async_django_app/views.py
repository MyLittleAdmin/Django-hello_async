import asyncio
import time

from django.shortcuts import render
from .async_scripts.sleep import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


async def do_async(request):
    asyncio.create_task(generate_file())
    context = {'time': time.strftime('%X')}
    return render(request, 'fuckoff.html', context=context)