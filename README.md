# Graphql Demo using python 'graphene-Django'

This Code explains how GraphQL works wiht graphene-Django module

### Prerquisites
- python3
- Django>=3.0.7
- graphene>=2.1.8

### code setup using VSCode in Windows
```sh
$cd workdir/
$mkdir medgraphql
$cd medgraphql
$django-admin startproject medgraphql .
$python manage.py makemigrations

$python manage.py migrate
```
#### Create the Django user
```sh
$python manage.py createsuperuser
$python manage.py startapp omquery
$python manage.py runserver 
```

###### To test Django project is running fine open the browser and end the url
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
#### Insert somedata either using manage.py loaddata <datafile> or using the shell like below
```sh
$python manage.py shell
$from omquery.models import CellOM, EnbOM

$EnbOM.objects.create(enb=1001, key='1001/20/10', om10=43254.44544, om11=34.45, om12=2)
$EnbOM.objects.create(enb=1002, key='1002/21/11', om10=34.34, om11=34.45, om12=676)
$EnbOM.objects.create(enb=1003, key='1003/22/12', om10=4, om11=67.90908, om12=10)
$EnbOM.objects.create(enb=1004, key='1004/23/13', om10=43254.78, om11=34.45, om12=2)
$EnbOM.objects.create(enb=1005, key='1005/24/14', om10=456.67, om11=34.45, om12=1)
$
$CellOM.objects.create(cellid=20, key='1001/cell/20', om1=343, om2=45, om3=454.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1001))
$CellOM.objects.create(cellid=21,key='1001/cell/21', om1=4565, om2=50, om3=67.65544, om4=7.0001, om5=30, enbom=EnbOM.objects.get(enb=1001))
$CellOM.objects.create(cellid=22,key='1003/cell/22', om1=343, om2=45, om3=454.6778, om4=3989.0001, om5=23, enbom=EnbOM.objects.get(enb=1003))
$CellOM.objects.create(cellid=23,key='1002/cell/20', om1=343, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
$CellOM.objects.create(cellid=24,key='1002/cell/20', om1=43, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
$CellOM.objects.create(cellid=25,key='1003/cell/20', om1=33, om2=45, om3=45345.6778, om4=3.0001, om5=34, enbom=EnbOM.objects.get(enb=1002))
$CellOM.objects.create(cellid=26,key='1004/cell/20', om1=143, om2=45, om3=45345.6778, om4=343.0001, om5=38, enbom=EnbOM.objects.get(enb=1002))
```

### setup graphql url in setting.py for developement
`urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
]`

### setup graphql url in setting.py for production
`urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
    path('admin/', admin.site.urls),
]`

### UI to test the graphQL
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

### sample request/response
--- Request1
```javascript
query allEnboms{
  allEnboms{
    enb
    key
  }
}
```
-- Response1
```javascript
{
  "data": {
    "allEnboms": [
      {
        "enb": 1001,
        "key": "1001/20/10"
      },
      {
        "enb": 1002,
        "key": "1002/21/11"
      },
      {
        "enb": 1003,
        "key": "1003/22/12"
      },
      {
        "enb": 1004,
        "key": "1004/23/13"
      },
      {
        "enb": 1005,
        "key": "1005/24/14"
      },
      {
        "enb": 1006,
        "key": "1006/34/45"
      }
    ]
  }
}
```

--- Request2
```javascript
mutation createEnbom{
  createEnbom(input: {enbid:1006, key:"1006/34/45"
  , om10:3432432.087, om11:78.68968,om12:89.7}){
    ok
    enb{
      enb
      key
    }
  }
}
```
--- Response2
```javascript
{
  "data": {
    "createEnbom": {
      "ok": true,
      "enb": {
        "enb": 1007,
        "key": "1006/34/45"
      }
    }
  }
}
```

