from django.shortcuts import render,get_object_or_404,redirect
from ert.models import Ert
from ert.forms import ErtForm

 

 
def home(request):
    """post index view"""
    
    return render(request,"ert/homepage.html",{ 'objectlist':Ert.objects.all() })
    
    
    
    
    
def details(request,pk):
    context_object={'category' : get_object_or_404(Ert,pk=pk)}
    template_name="ert/detail.html"
    return render(request, template_name,context_object)

    
    
    
    
      
def addErt(request):
    if(request.method=='POST'):
        ert_form=ErtForm(request.POST)
        if ert_form.is_valid():
            ert_form.save()
        return redirect('home')
            
    else:
        ert_form=ErtForm()
    return render(request,"ert/add_ert.html", {'form':ert_form })
  





 
 
def updateErt(request,pk):
    ert_object=get_object_or_404(Ert,pk=pk)
    ert_form=ErtForm(instance=ert_object)
    if(request.method=='POST'):
        ert_form=ErtForm(request.POST or None,instance=ert_object)
        if ert_form.is_valid():
            ert_form.save()
            return redirect('home')
    return render(request, 'ert/add_ert.html', {'form':ert_form })
   
 

 
def deleteErt(request, pk):
    delete_object=get_object_or_404(Ert,pk=pk)
    delete_object.delete()
    return redirect('home')
    

        
    
    