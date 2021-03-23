from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title = title, content = content)
        note.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    Note.objects.filter(id=id).delete()
    all_notes = Note.objects.all()
    return redirect('index')
    #return render(request, 'notes/index.html', {'notes': all_notes})

def edit(request, id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note.objects.filter(id=id).update(title=title, content=content)
        return redirect('index')
    else:  
        edit_note = Note.objects.get(id=id)
        print(edit_note)
        return render(request, 'notes/edit.html', {'note': edit_note})   
