from django.db import models

# Create your models here.

class branch_registration(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    branch_admin = models.CharField(max_length=100)
    branch_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def _str_(self):
        return self.branch_name



class designation(models.Model):
    branch =models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='designationbranch',null=True,blank=True)
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    def _str_(self):
        return self.designation


class department(models.Model):
    department=models.CharField(max_length=100)
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING , related_name='departmentbranch',null=True,blank=True)
    status=models.CharField(max_length=100)


    def _str_(self):
        return self.department


class create_team(models.Model):
    name = models.CharField(max_length=200) 
    trainer = models.CharField(max_length=200,default='')
    progress =  models.IntegerField() 
    status =  models.CharField(max_length=200)  


    def _str_(self):
        return self.name

class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240,null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='', default='')
    photo = models.FileField(upload_to='', default='')
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING, related_name='userregistrationdesignation',null=True,blank=True)
    department =models.ForeignKey(department, on_delete=models.DO_NOTHING, related_name='userregistrationdepartment',null=True,blank=True)
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='userregistrationbranch',null=True,blank=True)
    team = models.ForeignKey(create_team, on_delete=models.DO_NOTHING, related_name='userregistrationteam',null=True,blank=True)
    attitude = models.PositiveIntegerField(default='')
    creativity = models.PositiveIntegerField(default='')
    workperformance = models.PositiveIntegerField(default='')
    joiningdate =  models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    startdate =  models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate =  models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    status =  models.CharField(max_length=240, null=True,default='')

    
    def _str_(self):
        return self.fullname

class extracurricular(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='extracurricularuser',null=True,blank=True)
    internshipdetails = models.CharField(max_length=240,null=True)
    internshipduration = models.CharField(max_length=240,null=True)
    internshipcertificate = models.FileField(upload_to='', default='')
    onlinetrainingdetails = models.CharField(max_length=240,null=True)
    onlinetrainingduration = models.CharField(max_length=240,null=True)
    onlinetrainingcertificate= models.FileField(upload_to='', default='')
    projecttitle = models.CharField(max_length=240,null=True)
    projectduration = models.CharField(max_length=240,null=True)
    projectdescription = models.TextField(null=True)
    projecturl = models.CharField(max_length=240, default='',null=True,blank=True)
    skill1 = models.CharField(max_length=240, default='',null=True,blank=True)
    skill2 = models.CharField(max_length=240, default='',null=True,blank=True)
    skill3 = models.CharField(max_length=240, default='',null=True,blank=True)
    status = models.CharField(max_length=240,default='')
    
    
    def _str_(self):
        return self.projecttitle


class qualification(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='qualificationuser',null=True,blank=True)
    plustwo = models.CharField(max_length=240,null=True)
    schoolaggregate = models.CharField(max_length=240,null=True)
    schoolcertificate = models.FileField(upload_to='', default='')
    ugdegree = models.CharField(max_length=240,null=True)
    ugstream = models.CharField(max_length=240,null=True)
    ugpassoutyr = models.CharField(max_length=240,null=True)
    ugaggregrate = models.CharField(max_length=240,null=True)
    backlogs= models.CharField(max_length=240,null=True)
    ugcertificate = models.FileField(upload_to='', default='')
    pg= models.CharField(max_length=240,null=True)
    status = models.CharField(max_length=100,default='')


    def _str_(self):
        return self.user






class project(models.Model):
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='projectbranch',null=True,blank=True)
    department =models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='projectdepartment',null=True,blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='projectuser',null=True,blank=True)
    project = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startdate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    files=models.FileField(upload_to='', default='')
    status=models.CharField(max_length=100)
    

    def _str_(self):
        return self.project



class test_status(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='test_statususer',null=True,blank=True)
    project = models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='test_statusproject',null=True,blank=True)
    taskname = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='test_statustaskname',null=True,blank=True)
    date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    workdone = models.TextField(null=True)
    files=models.FileField(upload_to='', default='')


    def _str_(self):
        return self.project


class project_taskassign(models.Model):
    project = models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='project_taskassignproject',null=True,blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='project_taskassignuser',null=True,blank=True)
    tl = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='project_taskassigntl',null=True,blank=True)
    task = models.CharField(max_length=240)
    description = models.TextField()
    startdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    files=models.FileField(upload_to='', default='')
    department = models.CharField(max_length=200)#**************************
    designation = models.CharField(max_length=200)
    employee = models.CharField(max_length=200)
    tester = models.CharField(max_length=200)
    extension = models.IntegerField()
    reason = models.TextField()
    extension_status = models.CharField(max_length=200)
    tl_description = models.CharField(max_length=200)
    submitted_date= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    employee_files = models.FileField(upload_to='', default='')
    employee_description = models.TextField()
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.project


class tester_status(models.Model):
    tester = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='tester_statustester',null=True,blank=True)
    project =models.ForeignKey(project, on_delete=models.DO_NOTHING, related_name='tester_statusproject',null=True,blank=True)
    task = models.ForeignKey(project_taskassign, on_delete=models.DO_NOTHING, related_name='tester_statustask',null=True,blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='tester_statususer',null=True,blank=True)
    date= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    workdone = models.TextField()
    files=models.FileField(upload_to='', default='')
    subtask = models.TextField()
    progress = models.IntegerField()
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.project


class reported_issue(models.Model):
    reporter = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='reported_issuereporter',null=True,blank=True)
    reported_to = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='reported_issuereported_to',null=True,blank=True)
    issue = models.TextField()
    reported_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    reply = models.TextField()
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.reporter

    
class attendance(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='attendanceuser',null=True,blank=True)
    date= models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.user


class leave(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='leaveuser',null=True,blank=True)
    from_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date =  models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.user


class internship(models.Model):
    reg_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    fullname = models.CharField(max_length=200) 
    collegename = models.CharField(max_length=200) 
    reg_no = models.CharField(max_length=200) 
    course = models.CharField(max_length=200) 
    stream = models.CharField(max_length=200)
    branch = models.ForeignKey(branch_registration, on_delete=models.DO_NOTHING, related_name='internshipbranch',null=True,blank=True)
    platform = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    alternative_no = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic= models.ImageField(upload_to='' ,null=True)
    attach_file= models.FileField(default="")  
    rating = models.CharField(max_length=200)  
    hrmanager = models.CharField(max_length=200)
    guide = models.CharField(max_length=200)
    qr = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200)


    def _str_(self):
        return self.fullname




class trainer_task(models.Model):
    trainee = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='trainer_tasktrainee',null=True,blank=True)
    trainer = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='trainer_tasktrainer',null=True,blank=True)
    taskname =  models.CharField(max_length=240)
    startdate= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    files=models.FileField(upload_to='', default='')
    description = models.TextField()
    trainee_description = models.TextField()
    trainee_files = models.FileField(upload_to='', default='')
    status =  models.CharField(max_length=200)  


    def _str_(self):
        return self.trainee


class topic(models.Model):
    trainer = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='topictrainer',null=True,blank=True)
    team = models.ForeignKey(create_team, on_delete=models.DO_NOTHING, related_name='topicteam',null=True,blank=True)
    topic = models.CharField(max_length=240)
    startdate= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    files=models.FileField(upload_to='', default='')
    description = models.TextField()
    review = models.TextField()
    status =  models.CharField(max_length=200)


    def _str_(self):
        return self.topic