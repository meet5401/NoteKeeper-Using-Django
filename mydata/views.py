from django.shortcuts import render 
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .forms import AddNoteForm,  RegsiterNoteUserForm 
from django.contrib import messages
from .models import Info
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        
        if form.is_valid():
          
            notetitle = form.cleaned_data.get('title')
            notecontent = form.cleaned_data.get('content')
            notecretaedate = form.cleaned_data.get('created_date')
            noteupdateddate = form.cleaned_data.get('updated_date')
            usr = request.user

            qry = Info.objects.create(title= notetitle,content= notecontent,created_date=notecretaedate,updated_date=noteupdateddate, note_user=usr)
            qry.save()
            messages.success(request, f'Note Added For {notetitle} ')
            return redirect('index')        
    else :
        form = AddNoteForm()
        usr = request.user
    mynotes = Info.objects.filter(note_user=request.user).order_by('-pk')

    context = {'form': form, 'notes': mynotes}
    return render(request, 'index.html', context )

@login_required
def delete_note(request, pk ):
     todelete_note = list(Info.objects.filter(pk=pk))
     
     for dn in todelete_note:
        title = dn.title        
     Info.objects.filter(pk=pk).delete()
     messages.warning(request, f'Note Deleted For {title}')
     return redirect('index')

@login_required
def edit_note(request, pk):
    toedit_note = list(Info.objects.filter(pk=pk))
    for en in toedit_note:
        title = en.title 
        content = en.content
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            notetitle = form.cleaned_data.get('title')
            notecontent = form.cleaned_data.get('content')
            notecreateddate = form.cleaned_data.get('created_date')
            noteediteddate = form.cleaned_data.get('updated_date')
            usr = request.user
            qry = Info.objects.create(title=notetitle,content=notecontent,created_date=notecreateddate,updated_date=noteediteddate,note_user=usr)
            qry.save()
            Info.objects.filter(pk=pk).delete()
            return redirect('index')
    else:
        form = AddNoteForm({
            'title':title,                      
            'content':content,
        })  
    context = {'form': form, 'notes': Info.objects.filter(note_user=request.user).order_by('-pk')}  
    return render(request,'index.html',context)

# USER SECTION
def user_register(request):
    if request.method == 'POST':
        form = RegsiterNoteUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= RegsiterNoteUserForm()
    
    context = {'form':form}
    return render(request,'register.html',context)        

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            form_username = form.cleaned_data.get('username')
            form_password = form.cleaned_data.get('password')
            user_authobj = authenticate(username=form_username,password=form_password)
            if user_authobj is not None:
                login(request,user_authobj)
                return redirect('index')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'login.html',context)                    

def user_logout(request):
    logout(request)
    return redirect('login')