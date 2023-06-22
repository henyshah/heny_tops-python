from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        scount=SocietyMember.objects.all().count()
        if uid.role=="chairman":   
            cid=Chairman.objects.get(user_id=uid)
            context={
                    "uid":uid,
                    "cid":cid,
                    "scount":scount,
                }
            return render(request,"chairman/index.html",context)
        else:
            sid=SocietyMember.objects.get(user_id=uid)
            context={
                    "uid":uid,
                    "sid":sid,
                    "scount":scount,
                }
            return render(request,"chairman/s_index.html",context)
    else:
        return request(request,'chairman/login.html')

def login(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":   
            cid=Chairman.objects.get(user_id=uid)
            context={
                    "uid":uid,
                    "cid":cid,
                }
            return render(request,"chairman/index.html",context)
        else:
            sid=SocietyMember.objects.get(user_id=uid)
            context={
                    "uid":uid,
                    "sid":sid,
                }
            return render(request,"chairman/s_index.html",context)
    else:

        if request.POST:
            print("===>Login form submitted")
            p_email=request.POST['email']
            p_password=request.POST['password']

            try:
                uid=User.objects.get(email=p_email)

                if uid.password==p_password:
                    if uid.role=="chairman":
                        cid=Chairman.objects.get(user_id=uid)
                        print("===> FIRST NAME: ",cid.firstname)

                        request.session['email']=uid.email
                        context={
                            "uid":uid,
                            "cid":cid,
                            }
                        return render(request,"chairman/index.html",context)
                    else:
                       sid=SocietyMember.objects.get(user_id=uid)
                       request.session['email']=uid.email
                    context={
                            "uid":uid,
                            "sid":sid,
                        }
                    return render(request,"chairman/s_index.html",context)
                    
                else:
                    msg="Invalid Password"
                    context={
                        "msg":msg,
                        }
                    return render(request,"chairman/login.html",context)


                # print("===>response: ",uid)
                # print("===>email= ",p_email)
                # print("===>password= ",p_password)
            except:
                # print("===>Invalid Email or Paasword")
                msg="Invalid Email or Paasword"
                context={
                        "msg":msg,
                        }
                return render(request,"chairman/login.html",context)

        else:
            print("===>Login form refreshed")
        return render(request,"chairman/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"chairman/login.html")
    else:
        return render(request,"chairman/login.html")
    
def profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":   
            cid=Chairman.objects.get(user_id=uid)
            context={
                    "uid":uid,
                    "cid":cid,
                }
        return render(request,"chairman/profile.html",context)
    else:
        return render(request,"chairman/login.html")
    
    
def change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cpassword=request.POST['currentpassword']
        npassword=request.POST['newpassword']
        if uid.password==cpassword:
            uid.password=npassword
            uid.save() #update
            print("saved")
            del request.session['email']
            return render(request,"chairman/login.html")
        else: 
            pass
            
    else:
        return render(request,"chairman/login.html")
    
def update_chairman_profile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:

                cid.firstname=request.POST['firstname']
                cid.lastname=request.POST['lastname']
                cid.house_no=request.POST['house_no']
                cid.contact_no=request.POST['contact_no']

                if "mypicture" in request.FILES:
                    cid.pic = request.FILES['mypicture']
                    cid.save()


                cid.save() #update
                context={
                    "uid":uid,
                    "cid":cid
                }
                return render (request,"chairman/profile.html",context)
        else:
            pass
    else:
        return render(request,"chairman/login.html")
    return render(request,"chairman/login.html")
    
def add_media(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            medianame=request.POST['medianame']
            mediafile=request.FILES['mediafile']
            if medianame=="Image":
                eid=EventGallery.objects.create(user_id=uid,media_type=medianame,pic=mediafile)
            else:
                eid=EventGallery.objects.create(user_id=uid,media_type=medianame,videofile=mediafile)
            eid=EventGallery.objects.create(user_id=uid,media_type=medianame,videofile=mediafile)
            context={
                "uid":uid,
                "cid":cid,
                'msg':"Successfully media uploaded"           
              }
            return render (request,"chairman/add_media.html",context)
        else:
            context={
                    "uid":uid,
                    "cid":cid,
                               
                }
            return render (request,"chairman/add_media.html",context)

    else:
        return render(request,"chairman/login.html")


def view_image_gallery(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            img_all=EventGallery.objects.filter(media_type="Image")
            context={
                "uid":uid,
                "cid":cid,
                "img_all":img_all,  
            }
            return render(request,"chairman/image-gallery.html",context)
        else:
            pass
        return render(request,"chairman/image-gallery.html")
    else:
        return render(request,"chairman/login.html")
    

def view_video_gallery(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            video_all=EventGallery.objects.filter(media_type="Video")
            context={
                "uid":uid,
                "cid":cid,
                "video_all":video_all,  
            }
            return render(request,"chairman/video-gallery.html",context)
        else:
            pass
        return render(request,"chairman/video-gallery.html")
    else:
        return render(request,"chairman/login.html")
    
def delete_video(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            videoid=EventGallery.objects.get(id=pk)
            videoid.delete()
            video_all=EventGallery.objects.filter(media_type="Video")
            context={
                "uid":uid,
                "cid":cid,
                "video_all":video_all,  
            }
            return render(request,"chairman/video-gallery.html",context)

    
def add_member(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:
                muserid=User.objects.create(email=request.POST['email'],
                                            password=request.POST['password'],
                                            role="SocietyMember")
                if"pic" in request.FILES:
                    sid=SocietyMember.objects.create(user_id=uid,
                                                    firstname=request.POST['firstname'],
                                                    lastname=request.POST['lastname'],
                                                    house_no=request.POST['house_no'],
                                                    contact_no=request.POST['contact_no'],
                                                    blood_group=request.POST['blood_group'],
                                                    job_description=request.POST['job_description'],
                                                    job_address=request.POST['job_address'],
                                                    no_of_familymembers=request.POST['no_of_familymembers'],
                                                    vehicle_details=request.POST['vehicle_details'],
                                                    pic=request.FILES['pic'],
                                                    )
                else:
                    sid=SocietyMember.objects.create(user_id=uid,
                                                    firstname=request.POST['firstname'],
                                                    lastname=request.POST['lastname'],
                                                    house_no=request.POST['house_no'],
                                                    contact_no=request.POST['contact_no'],
                                                    blood_group=request.POST['blood_group'],
                                                    job_description=request.POST['job_description'],
                                                    job_address=request.POST['job_address'],
                                                    no_of_familymembers=request.POST['no_of_familymembers'],
                                                    vehicle_details=request.POST['vehicle_details'],
                                                    )
                msg="Successfully member created !"
                context={
                    "uid":uid,
                    "cid":cid, 
                    "msg":msg,           
                }
                return render(request,"chairman/add-member.html",context)
            else:
                context={
                    "uid":uid,
                    "cid":cid,            
                }
                return render(request,"chairman/add-member.html",context)
    else:
        return render(request,"chairman/login.html")
            

def all_member(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="chairman":
            cid=Chairman.objects.get(user_id=uid)

            sall=SocietyMember.objects.all()
            context={
                "uid":uid,
                "cid":cid, 
                "sall":sall,
            }
            return render(request,"chairman/members.html",context)


def sall_member(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="SocietyMember":
            sid=SocietyMember.objects.get(user_id=uid)

            sall=SocietyMember.objects.all().exclude(user_id=uid)
            context={
                "uid":uid,
                "sid":sid, 
                "sall":sall,
            }
            return render(request,"chairman/s_members.html",context)


def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            
        if request.POST:
            medianame = request.POST['medianame']
            mediafile = request.FILES['mediafile']
            if medianame == "Image":
                eid = Notice.objects.create(user_id = uid,media_type = medianame,pic = mediafile)
            else:
                eid = Notice.objects.create(user_id = uid,media_type = medianame,videofile = mediafile)
                                              
                                                  
            context = {
                'uid' : uid,
                'cid' : cid,
                'msg' : " notice uploaded successfully! "
            }
            return render(request,"chairman/add_notice.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairman/add_notice.html",context)
             
    else:
        return render(request,"chairman/login.html")
    

def all_notice(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])        
       if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            n_all = Notice.objects.filter(media_type = "Image")
            context = {
            'uid' : uid,
            'cid' : cid,
            'n_all' : n_all,
            }
            return render(request,"chairman/all-notice.html",context)
       else:
            pass    
       return render(request,"chairman/all-notice.html")
    else:
        return render(request,"chairman/login.html")
    


def Society_Member_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "SocietyMember":
                sid = SocietyMember.objects.get(user_id = uid)
                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
        return render(request,"chairman/s_profile.html",context)
    else:
        return render(request,"chairman/login.html")
    

def Society_Member_change_password(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        spassword = request.POST['surrentpassword']
        npassword = request.POST['newpassword']

        if uid.password == spassword:
            uid.password = npassword
            uid.save() #update
            del request.session['email']
            return render(request,"chairman/s_profile.html")
        else:
            pass            
    else:
        return render(request,"chairman/login.html")    


def Society_Member_update_chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])

        if uid.role == "SocietyMember":
            sid = SocietyMember.objects.get(user_id = uid)
            if request.POST:
                sid.firstname = request.POST['firstname']
                sid.lastname = request.POST['lastname']
                sid.house_no = request.POST['house_no']
                sid.contact_no = request.POST['contact_no']
                
                if "mypicture" in request.FILES:
                    sid.pic = request.FILES['mypicture']
                    sid.save() #update
                
                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
                return render(request,"chairman/s_profile.html",context)
            else:
                pass
        else:
            return render(request,"chairman/login.html")    
        return render(request,"chairman/login.html")
    

def Society_Member_view_image_gallery(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
        
       if uid.role == "SocietyMember":
            sid = SocietyMember.objects.get(user_id = uid)
            s_img_all = EventGallery.objects.filter(media_type = "Image")
            context = {
            'uid' : uid,
            'sid' : sid,
            's_img_all' : s_img_all,
            
            }
            return render(request,"chairman/s-image-gallery.html",context)

       else:
            pass    
       return render(request,"chairman/s-image-gallery.html")
    else:
        return render(request,"chairman/login.html")
    

def Society_Member_view_video_gallery(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
        
       if uid.role == "SocietyMember":
            sid = SocietyMember.objects.get(user_id = uid)
            s_video_all = EventGallery.objects.filter(media_type = "video")
            print("=====>>>>>")
            context = {
                'uid' : uid,
                'sid' : sid,
                's_video_all' : s_video_all,
            }
            print("====>>> video ",s_video_all)
            return render(request,"chairman/s-video-gallery.html",context)

       else:
            pass    
       return render(request,"chairman/s-video-gallery.html")
    else:
        return render(request,"chairman/login.html")
    

def sall_notice(request):
    if "email" in request.session:
       uid = User.objects.get(email = request.session['email'])
        
       if uid.role == "SocietyMember":
            sid = SocietyMember.objects.get(user_id = uid)
            s_n_all = Notice.objects.filter(media_type = "Image")
            context = {
            'uid' : uid,
            'sid' : sid,
            's_n_all' : s_n_all,
            
            }
            return render(request,"chairman/s-all-notice.html",context)

       else:
            pass    
       return render(request,"chairman/s-all-notice.html")
    else:
        return render(request,"chairman/login.html")    

def reg(request):
    return render(request,"chairman/registration_example.html")