from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.functions import Length

def equijoin(request):
    EMO=Emp.objects.select_related('deptno').all()
    #select_related for 1 to 1,t 10 many
    #it will join then it will retrive
    #prefetch_related for 1 to 1,1 to many,many to 1,many to many
    #it will fetch/retrive then join
    #deptno is common column
    EMO=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMO=Emp.objects.select_related('deptno').filter(sal__lt=4000)
    EMO=Emp.objects.select_related('deptno').filter(sal__gte=4000)
    EMO=Emp.objects.select_related('deptno').filter(sal__gt=4000)
    EMO=Emp.objects.select_related('deptno').filter(sal__gte=4000,sal__lt=5000)
    EMO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    #if mgr is not there we need to give isnull=True
    EMO=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    #false will get who and all have mgr
    EMO=Emp.objects.select_related('deptno').filter(ename='vicky')
    #EMO is emp table object,to get data from same table we r using columnname=value
    EMO=Emp.objects.select_related('deptno').filter(deptno__deptno=10)
    #for another table common column__columnname=value
    
    EMO=Emp.objects.select_related('deptno').filter(sal__gt=4000,sal__lt=5000)
    #for concatenation we are using comma like plus sym,pipe symbol
    EMO=Emp.objects.select_related('deptno').all()
    EMO=Emp.objects.select_related('deptno').filter(deptno__dloc='singapore')
    #print(EMO)
    #EMO=Emp.objects.select_related('deptno').filter(deptno__dname='ui/ux')
    EMO=Emp.objects.select_related('deptno').filter(ename='barath')
    
    d={'EMO' : EMO}
    return render (request,'equijoin.html',d)


    #for printing data
     #same table objectname.columnname,other table objname.commoncol.colname
    #for writing a condition
    # sametable colname=value,other table commonname__colname=value 



def selfjoin(request):
    EmpMgrObj=Emp.objects.select_related('mgr').all()
    #in html page we gave ename,mgr columns so we will get this 2 column data
    #if we give all th we will get all column details
    EmpMgrObj=Emp.objects.select_related('mgr').filter(ename='ramani')
    #we gave ename with value so that record will display
    EmpMgrObj=Emp.objects.select_related('mgr').filter(ename='yaswanth',sal__gte=5000)
    EmpMgrObj=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    EmpMgrObj=Emp.objects.select_related('mgr').filter(mgr__ename='vicky')
    #here vicky is mgr,who and all having vicky as mgr there details will display
    EmpMgrObj=Emp.objects.select_related('mgr').filter(mgr__ename='yaswanth')
    #EmpMgrObj=Emp.objects.select_related('mgr').filter(ename__mgr='barath')
    EmpMgrObj=Emp.objects.select_related('mgr').filter(ename='ramani',sal__lte=5000)
    #EmpMgrObj=Emp.objects.select_related('mgr').all() 
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by(Length('ename'))
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by(Length('ename').desc())
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by(Length('mgr').desc())
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by(Length('mgr'))
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by('empno')
    EmpMgrObj=Emp.objects.select_related('mgr').all().order_by('-empno')
    EmpMgrObj=Emp.objects.select_related('mgr').filter(ename__startswith='v')
    EmpMgrObj=Emp.objects.select_related('mgr').filter(ename__endswith='h')
    






    d={'EmpMgrObj':EmpMgrObj}
    return render(request,'selfjoins.html',d)    