# graphql-demo

> django-admin startproject <pj name> .


> python manage.py makemigrations
> python manage.py migrate

> python manage.py createsuperuser

> python manage.py startapp <appname>
> python manage.py runserver

> python manage.py shell

> from omquery.models import CellOM, EnbOM


> EnbOM.objects.create(enb=1001, key='1001/20/10', om10=43254.44544, om11=34.45, om12=2)
> EnbOM.objects.create(enb=1002, key='1002/21/11', om10=34.34, om11=34.45, om12=676)
> EnbOM.objects.create(enb=1003, key='1003/22/12', om10=4, om11=67.90908, om12=10)
> EnbOM.objects.create(enb=1004, key='1004/23/13', om10=43254.78, om11=34.45, om12=2)
> EnbOM.objects.create(enb=1005, key='1005/24/14', om10=456.67, om11=34.45, om12=1)

> CellOM.objects.create(cellid=20, key='1001/cell/20', om1=343, om2=45, om3=454.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1001))
> CellOM.objects.create(cellid=21,key='1001/cell/21', om1=4565, om2=50, om3=67.65544, om4=7.0001, om5=30, enbom=EnbOM.objects.get(enb=1001))
> CellOM.objects.create(cellid=22,key='1003/cell/22', om1=343, om2=45, om3=454.6778, om4=3989.0001, om5=23, enbom=EnbOM.objects.get(enb=1003))
> CellOM.objects.create(cellid=23,key='1002/cell/20', om1=343, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
> CellOM.objects.create(cellid=24,key='1002/cell/20', om1=43, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
> CellOM.objects.create(cellid=25,key='1003/cell/20', om1=33, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
> CellOM.objects.create(cellid=26,key='1004/cell/20', om1=143, om2=45, om3=45345.6778, om4=343.0001, om5=38, enbom=EnbOM.objects.get(enb=1002))
