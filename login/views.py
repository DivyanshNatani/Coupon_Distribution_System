from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse, HttpResponse
from login.models import userDetail
from django.contrib import messages
from coupons.models import couponsTable

isLogin = False
lastLoginID = None

# Create your views here.
def loginPage(request):
    messages.success(request, "Welcome to Mood Indigo CDS System!")
    return render(request,'memberlogin.html')

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
                    couponDetail = list(couponsTable.objects.values('allotedTo','venderName','id').filter(allotedTo=nameID).filter(allocationStatus='Using'))
                    post_reg = "Coordinator" if obj_child.userPost=="CG" else "Organiser"
                    if(post_reg == "Coordinator"):
                        userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').exclude(userPost="CG"))
                    else:
                        userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').filter(userPost=post_reg))
                    context = {"userID" : obj_child.userID,
                                "name" : obj_child.firstName,
                                "post" : obj_child.userPost,
                                "post_reg" : post_reg,
                                "detail" : couponDetail,
                                "userUnder" : userUnder
                                }
                    # print("Yes", userDetail.userID, userDetail.password)
                    if(post_reg == "Coordinator" or obj_child.userPost == "Coordinator"):
                        return render(request, 'home.html', context)
                    else:
                        messages.warning(request, "Please login to CDS coupon portal to use Coupons.")
                        return HttpResponseRedirect('/cds/')
                else:
                    messages.warning(request, "Invalid UserID/Password")
                    return render(request, 'memberlogin.html')

            messages.warning(request, "Invalid UserID/Password")
            return render(request, 'memberlogin.html')
            

        elif "register" in request.POST:
            # print("I am in register")
            nameID = request.POST.get('userID')
            obj=userDetail.objects
            obj=obj.filter(userID=nameID)
            obj1=userDetail.objects
            obj1=obj1.filter(userID=request.POST.get('orignalUserID'))
            couponDetail = list(couponsTable.objects.values('allotedTo','venderName', 'id').filter(allotedTo=obj1[0].userID).filter(allocationStatus='Using'))
            post_reg = "Coordinator" if obj1[0].userPost=="CG" else "Organiser"
            if(post_reg == "Coordinator"):
                userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').exclude(userPost="CG"))
            else:
                userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').filter(userPost=post_reg))
            context = {"userID" : obj1[0].userID,
                            "name" : obj1[0].firstName,
                            "post" : obj1[0].userPost,
                            "post_reg" : post_reg,
                            "detail" : couponDetail,
                            "userUnder" : userUnder
                        }

            for obj_child in obj:
                
                messages.warning(request, "User ID already exists. Please choose new User ID")
                # print("Contact not saved")
                # print("Yes", userDetail.userID, userDetail.password)
                return render(request, 'home.html', context)
                # print(obj[0])
            
            fname = request.POST.get('fName')
            lname = request.POST.get('lName')
            pas= request.POST.get('password')
            phNo= request.POST.get('mobileNo')
            post_app= request.POST.get('post_app')
            # print(post_app)
            try:

                b=userDetail(userID=nameID, password=pas, firstName=fname, lastName=lname, mobNumber=phNo, userPost=post_app)
                b.save()
                if(post_reg == "Coordinator"):
                    context["userUnder"] = list(userDetail.objects.values('userID', 'firstName', 'lastName').exclude(userPost="CG"))
                else:
                    context["userUnder"] = list(userDetail.objects.values('userID', 'firstName', 'lastName').filter(userPost=post_reg))
            except:
                messages.warning(request, "Invalid entry. Please try again")
                return render(request, 'home.html', context)
            # print("saved")
            messages.success(request, fname + " successfully registered!!")
            return render(request, 'home.html', context)

        elif "reallocate" in request.POST:
            nameID = request.POST.get('userID')
            post_reg = request.POST.get('post_app')
            obj=userDetail.objects
            obj1=obj.filter(userID=nameID)
            
            coupon = int(request.POST.get("coupon"))
            targetID = request.POST.get('aName')

            b = couponsTable.objects.get(id=coupon)
            b.allotedTo = targetID
            b.save()
            messages.success(request,"Coupon No"+ str(coupon) + "successfully transfered to "+ targetID)
            
            
            couponDetail = list(couponsTable.objects.values('allotedTo','venderName','id').filter(allotedTo=nameID).filter(allocationStatus='Using'))
            # post_reg = "Coordinator" if obj_child.userPost=="CG" else "Organisor"
            post_reg = "Coordinator" if obj1[0].userPost=="CG" else "Organiser"
            if(post_reg == "Coordinator"):
                userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').exclude(userPost="CG"))
            else:
                userUnder = list(userDetail.objects.values('userID', 'firstName', 'lastName').filter(userPost=post_reg))
            context = {"userID" : obj1[0].userID,
                    "name" : obj1[0].firstName,
                    "post" : obj1[0].userPost,
                    "post_reg" : post_reg,
                    "detail" : couponDetail,
                    "userUnder" : userUnder
                    }
            return render(request, 'home.html', context)

    
    return render(request, 'memberlogin.html')            










            

    # return render(request,'login/')
