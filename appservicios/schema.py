import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from appservicios.models import Cliente, Servicios, Contratos, Usuario

class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente

class ServiciosType(DjangoObjectType):
    class Meta:
        model = Servicios

class ContratosType(DjangoObjectType):
    class Meta:
        model = Contratos
    
class UsuariosType(DjangoObjectType):
    class Meta:
        model = Usuario
    
class Query(ObjectType):
    cliente = graphene.Field(ClienteType, id=graphene.Int())
    servicio = graphene.Field(ServiciosType, id=graphene.Int())
    contrato = graphene.Field(ContratosType, id=graphene.Int())
    usuario = graphene.Field(UsuariosType, id=graphene.Int())
    clientes = graphene.List(ClienteType)
    servicios = graphene.List(ServiciosType)
    contratos = graphene.List(ContratosType)
    usuarios = graphene.List(UsuariosType)

    def resolve_cliente(self,info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Cliente.objects.get(pk=id)
        
        return None

    def resolve_servicio(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Servicios.objects.get(pk=id)
        
        return None
    
    def resolve_contrato(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Contratos.objects.get(pk=id)

        return None

    def resolve_usuario(self,info,**kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Usuario.objects.get(pk=id)
        
        return None
    
    def resolve_clientes(self, info, **kwargs):
        return Cliente.objects.all()

    def resolve_servicios(self, info, **kwargs):
        return Servicios.objects.all()

    def resolve_contratos(self, info, **kwargs):
        return Contratos.objects.all()
    
    def resolve_usuarios(self, info, **kwargs):
        return Usuario.objects.all()
    

class ClienteInput(graphene.InputObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    apellido = graphene.String()
    edad = graphene.Int()
    telefono = graphene.String()
    email = graphene.String()

class ServicioInput(graphene.InputObjectType):
    id = graphene.ID()
    servicio = graphene.String()
    descripcion = graphene.String()

class ContratoInput(graphene.InputObjectType):
    id = graphene.ID()
    fecha = graphene.Date()
    costo = graphene.Int()
    clientes = graphene.List(ClienteInput)
    Servicios = graphene.List(ServicioInput)

class UsuarioInput(graphene.InputObjectType):
    id = graphene.ID()
    usuario = graphene.String()
    password = graphene.String()

class CreateCliente(graphene.Mutation):
    class Arguments:
        input = ClienteInput(required=True)
    ok = graphene.Boolean()
    cliente = graphene.Field(ClienteType)
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        cliente_instance = Cliente(nombre=input.nombre, apellido=input.apellido, edad=input.edad, telefono=input.telefono, email=input.email)
        cliente_instance.save()
        return CreateCliente(ok=ok, cliente=cliente_instance)
    
    class UpdateCliente(graphene.Mutation):
        class Arguments:
            id = graphene.Int(required=True)
            input = ClienteInput(required=True)
        
        ok = graphene.Boolean()
        cliente = graphene.Field(ClienteType)
        @staticmethod
        def mutate(root, info, id, input=None):
            ok = False
            if cliente_instance:
                ok = True
                cliente_instance.nombre = input.nombre
                cliente_instance.apellido = input.apellido
                cliente_instance.edad = input.edad
                cliente_instance.telefono = input.telefono
                cliente_instance.email = input.email
                cliente_instance.save()
                return UpdateCliente(ok=ok, cliente=cliente_instance)
            return UpdateCliente(ok=ok, cliente=None)