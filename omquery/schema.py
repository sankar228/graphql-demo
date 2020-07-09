import graphene
import graphene.relay as relay
from graphene_django.filter.fields import DjangoFilterConnectionField

from graphene_django.types import DjangoObjectType, ObjectType
from omquery.models import EnbOM, CellOM, NimsTmus
import decimal

#Query
class NimsTmusType(DjangoObjectType):
    class Meta:
        model = NimsTmus
        filter_fields = ['technology', 'site_name', 'vendor', 'cellname', 'oss_market']
        interfaces = (relay.Node,)
        
class CellOMType(DjangoObjectType):
    class Meta:
        model = CellOM

class EnbOMType(DjangoObjectType):
    class Meta:
        model = EnbOM
        
#Query
class Query(graphene.ObjectType):        
    ##Query all the records from the DB
    all_nims = graphene.List(NimsTmusType)
    def resolve_all_nims(self, info, **kwargs):
        return NimsTmus.objects.all()
    
    ##Connect to Relay Node to apply filter filds and pagination
    all_nimsrecs = DjangoFilterConnectionField(NimsTmusType)
    
    all_celloms = graphene.List(CellOMType)
    def resolve_all_celloms(self, info, **kwargs):
        return CellOM.objects.select_related('enb').all()
    
    all_enboms = graphene.List(EnbOMType)
    def resolve_all_enboms(self, info, **kwargs):
        return EnbOM.objects.all()
    
    cellom = graphene.Field(CellOMType, cellid=graphene.Int())
    def resolve_cellom(self, info, **kwargs):
        cellid = kwargs.get('cellid')
        if cellid is not None:
            return CellOM.objects.get(cellid=cellid)
        
    enbom = graphene.Field(EnbOMType, enb=graphene.Int())  
    def resolve_enbom(self, info, **kwargs):
        enb = kwargs.get('enb')
        if enb is not None:
            return EnbOM.objects.get(enb=enb)
    
    

#Mutations
class EnbOMInput(graphene.InputObjectType):
    enbid  = graphene.Int()
    key  = graphene.String()
    om10 = graphene.Float()
    om11 = graphene.Float()
    om12 = graphene.Float()
    
class CreateEnbOM(graphene.Mutation):
    ok = graphene.Boolean()
    enb = graphene.Field(EnbOMType)
    
    class Arguments:
        input = EnbOMInput(required=True)         
    
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        enb_obj = EnbOM(enb=input.enbid, key=input.key, om10= input.om10, om11= input.om11, om12= input.om12)
        enb_obj.save()
        
        return CreateEnbOM(ok= ok, enb = enb_obj)


class Mutation(graphene.ObjectType):
    create_enbom = CreateEnbOM.Field()