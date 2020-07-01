import graphene

from graphene_django.types import DjangoObjectType
from omquery.models import EnbOM, CellOM

class CellOMType(DjangoObjectType):
    class Meta:
        model = CellOM

class EnbOMType(DjangoObjectType):
    class Meta:
        model = EnbOM
        

class Query(object):
    celloms = graphene.Field(CellOMType, cellid=graphene.Int())
    enboms = graphene.Field(CellOMType, enb=graphene.Int()) 
    all_celloms = graphene.List(CellOMType)
    all_enboms = graphene.List(EnbOMType)
    
    def resolve_celloms(self, info, **kwargs):
        cellid = kwargs.get('cellid')
        if cellid is not None:
            return CellOM.objects.get(cellid=cellid)   
        
    
    def resolve_enboms(self, info, **kwargs):
        enb = kwargs.get('enb')
        if enb is not None:
            return EnbOM.objects.get(enb=enb)
    
    def resolve_all_celloms(self, info, **kwargs):
        return CellOM.objects.select_related('enb').all()
    
    def resolve_all_enboms(self, info, **kwargs):
        return EnbOM.objects.all()
        