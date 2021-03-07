from django.shortcuts import render, HttpResponse
from vender.models import venderTable
from login.models import userDetail
from django.contrib import messages
from coupons.models import couponsTable

# Create your views here.
def loginCheck(request):
    ven_name = list(venderTable.objects.values('venderName'))
    # ven_name = Entry.objects.values_list('venderName')
    # print(ven_name)
    # print(list(ven_name))
    context = {
        "vender_name" : ven_name
    }


    if request.method == 'POST':
        if "vender_reg" in request.POST:
            v_name=request.POST.get('venderID')
            pas=request.POST.get('password')
            cont=request.POST.get('contactDetail')
            try:
                b=venderTable(venderName=v_name, password=pas, contectNumber=cont)
                b.save()
                messages.success(request, v_name + " vender successfully registered")
            except:
                    messages.warning(request, "Invalid entry. Please try again")
                    return render(request, 'fnb.html', context)

        elif "register" in request.POST:
            # print("I am in register")
            nameID = request.POST.get('userID')
            obj=userDetail.objects
            obj=obj.filter(userID=nameID)
            # obj1=userDetail.objects
            # obj1=obj1.filter(userID=request.POST.get('orignalUserID'))
            # context = {"userID" : obj1[0].userID,
            #                 "name" : obj1[0].firstName,
            #                 "post" : obj1[0].userPost,
            #                 "post_reg" : "Coordinator" if obj1[0].userPost=="CG" else "Organisor",
            #             }

            for obj_child in obj:
                
                messages.warning(request, "User ID already exists. Please choose new User ID")
                # print("Contact not saved")
                # print("Yes", userDetail.userID, userDetail.password)
                return render(request, 'fnb.html', context)
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
            except:
                messages.warning(request, "Invalid entry. Please try again")
                return render(request, 'fnb.html', context)
            # print("saved")
            messages.success(request, fname + " successfully registered!!")
            return render(request, 'fnb.html', context)
        elif "coupon_reg" in request.POST:
            venderName=request.POST.get('vName')
            numCoupons=int(request.POST.get('noCoupons'))
            # print(venderName, numCoupons)
            cg_names = list(userDetail.objects.values('userID').filter(userPost='CG'))
            totnum=len(cg_names)
            # print((cg_names[0])['userID'])
            for i in range(totnum*numCoupons):
                cg = (cg_names[i%totnum])['userID']

                b=couponsTable(allotedTo=cg, venderName=venderName)
                b.save()
                
            messages.success(request, str(i+1) + " Coupons Successfully Registered!!")


            return render(request, 'fnb.html', context)
    
    # print("default")
    return render(request, 'fnb.html', context)




