from django.shortcuts import render, redirect
from .forms import PersonaForm

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')  
    else:
        form = PersonaForm()
    
    return render(request, 'crear_persona.html', {'form': form})
