from django.shortcuts import render
from login.models import userDetail
from django.contrib import messages

# Create your views here.
def loginCheck(request):
    if request.method == 'POST':
        if "login" in request.POST:
            nameID = request.POST.get('userID')
            password = request.POST.get('password')
            # print(nameID, password)
            obj=userDetail.objects
            obj=obj.filter(userID=nameID)
            # print(obj[0].password)
            for obj_child in obj:
                if obj_child.password == password :
                    context = {"userID" : obj_child.userID,
                                "name" : obj_child.firstName,
                                "post" : obj_child.userPost,
                                "post_reg" : "Coordinator" if obj_child.userPost=="CG" else "Organisor"
                                }
                    # print("Yes", userDetail.userID, userDetail.password)
                    return render(request, 'cds.html', context)
                else:
                    messages.warning(request, "Invalid UserID/Password")
                    return render(request, 'cdslogin.html')

            messages.warning(request, "Invalid UserID/Password")
            return render(request, 'cdslogin.html')
    
    return render(request, 'cdslogin.html')
            

        # elif "register" in request.POST:
        #     # print("I am in register")
        #     nameID = request.POST.get('userID')
        #     obj=userDetail.objects
        #     obj=obj.filter(userID=nameID)
        #     obj1=userDetail.objects
        #     obj1=obj1.filter(userID=request.POST.get('orignalUserID'))
        #     context = {"userID" : obj1[0].userID,
        #                     "name" : obj1[0].firstName,
        #                     "post" : obj1[0].userPost,
        #                     "post_reg" : "Coordinator" if obj1[0].userPost=="CG" else "Organisor",
        #                 }

        #     for obj_child in obj:
                
        #         messages.warning(request, "User ID already exists. Please choose new User ID")
        #         # print("Contact not saved")
        #         # print("Yes", userDetail.userID, userDetail.password)
        #         return render(request, 'home.html', context)
        #         # print(obj[0])
            
        #     fname = request.POST.get('fName')
        #     lname = request.POST.get('lName')
        #     pas= request.POST.get('password')
        #     phNo= request.POST.get('mobileNo')
        #     post_app= request.POST.get('post_app')
        #     # print(post_app)
        #     try:

        #         b=userDetail(userID=nameID, password=pas, firstName=fname, lastName=lname, mobNumber=phNo, userPost=post_app)
        #         b.save()
        #     except:
        #         messages.warning(request, "Invalid entry. Please try again")
        #         return render(request, 'home.html', context)
        #     # print("saved")
        #     messages.success(request, fname + " successfully registered!!")
        #     return render(request, 'home.html', context)
