from django.shortcuts import render,redirect
from .models import Comment

# Create your views here.
def contact(request):
    if request.method=='POST':
        f_name=request.POST["firstname"]
        l_name=request.POST["lastname"]
        tel_number=request.POST["telnum"]
        areacode=request.POST["areacode"]
        email=request.POST["email"]
        feedback=request.POST["feedback"]
        approve=request.POST["approve"]
        tel_email=request.POST["Tel_email"]

        tel_num="+"+ areacode+ " "+tel_number
        if approve=="approve":
            if tel_email=="tel":
                tel_email="tel"
            
            else:
                tel_email="email"
            approve=True
            return tel_email,approve
        else:
            tel_email=None
            approve=False
            
        comment = Comment(first_name=f_name, last_name=l_name,tel_number=tel_num,email=email,contact_me=approve,contact_me_by=tel_email,feedback=feedback)

        comment.save()
        return redirect('/')
    else:
        return render(request,"contactus.html")