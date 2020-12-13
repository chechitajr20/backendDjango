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

    def resolve_cliente(self, info, **kwargs):
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

    def resolve_usuario(self, info, **kwargs):
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
        cliente_instance = Cliente(nombre=input.nombre, apellido=input.apellido,
                                   edad=input.edad, telefono=input.telefono, email=input.email)
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
        cliente_instance = Cliente.objects.get(pk=id)
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

class CreateServicio(graphene.Mutation):
    class Arguments:
        input = ServicioInput(required=True)
    
    ok = graphene.Boolean()
    servicio = graphene.Field(ServiciosType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        servicio_instance = Servicios(servicio = input.servicio, descripcion = input.descripcion)
        servicio_instance.save()
        return CreateServicio(ok=ok, servicio=servicio_instance)

class UpdateServicio(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ServicioInput(required=True)
    
    ok = graphene.Boolean()
    servicio = graphene.Field(ServiciosType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        servicio_instance = Servicios.objects.get(pk=id)
        if servicio_instance:
            ok = True
            servicio_instance.servicio = input.servicio
            servicio_instance.descripcion = input.descripcion
            servicio_instance.save()
            return UpdateServicio(ok=ok, servicio=servicio_instance)
        return UpdateServicio(ok=ok, servicio=None)

class CreateUsuario(graphene.Mutation):
    class Arguments:
        input = UsuarioInput(required=True)
    
    ok = graphene.Boolean()
    usuario = graphene.Field(UsuariosType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        usuario_instance = Usuario(usuario=input.usuario, password=input.password)
        usuario_instance.save()
        return CreateUsuario(ok=ok, usuario=usuario_instance)

class UpdateUsuario(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UsuarioInput(required=True)

    ok = graphene.Boolean()
    usuario = graphene.Field(UsuariosType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        usuario_instance = Usuario.objects.get(pk=id)
        if usuario_instance:
            ok = True
            usuario_instance.usuario = input.usuario
            usuario_instance.password = input.password
            usuario_instance.save()
            return UpdateUsuario(ok=ok, usuario=usuario_instance)
        return UpdateUsuario(ok=ok, usuario=None)

class CreateContratos(graphene.Mutation):
    class Arguments:
        input = ContratoInput(required=True)

    ok = graphene.Boolean()
    contrato = graphene.Field(ContratosType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        clientes = []
        servicios = []

        for cliente_input in input.clientes:
            cliente = Cliente.objects.get(pk=cliente_input.id)
            if cliente is None:
                return CreateContratos(ok=False, contrato=None)
            clientes.append(cliente)

        for servicio_input in input.servicios:
            servicio = Servicios.objects.get(pk=servicio_input.id)
            if servicio is None:
                return CreateContratos(ok=False, contrato=None)
            servicios.append(servicio)

        contrato_instance = Contratos(
            fecha = input.fecha,
            costo = input.costo
            )
        contrato_instance.save()
        contrato_instance.clientes.set(clientes)
        return CreateContratos(ok=ok, contrato=contrato_instance)

class UpdateContrato(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ContratoInput(required=True)
    ok = graphene.Boolean()
    contrato = graphene.Field(ContratosType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        contrato_instance = Contratos.objects.get(pk=id)
        if contrato_instance:
            ok = True
            clientes = []
            servicios = []
            for cliente_input in input.clientes:
                cliente = Cliente.objects.get(pk=cliente_input.id)
                if cliente is None:
                    return UpdateContrato(ok=False,contrato=None)
                clientes.append(cliente)
            
            for servicio_input in input.servicios:
                servicio = Servicios.objects.get(pk=servicio_input.id)
                if servicio is None:
                    return UpdateContrato(ok=False, contrato=None)
                servicios.append(servicio)
            
            contrato_instance.fecha = input.fecha
            contrato_instance.costo = input.costo
            contrato_instance.save()
            contrato_instance.clientes.set(clientes)
            contrato_instance.servicios.set(servicios)
            return UpdateContrato(ok=ok, contrato=contrato_instance)
        return UpdateContrato(ok=ok, contrato=None)

class Mutation(graphene.ObjectType):
    create_cliente = CreateCliente.Field()
    update_cliente = UpdateCliente.Field()
    create_servicio = CreateServicio.Field()
    update_servicio = UpdateServicio.Field()
    create_usuario = CreateUsuario.Field()
    update_usuario = UpdateUsuario.Field()
    create_contrato = CreateContratos.Field()
    update_contrato = UpdateContrato.Field()
schema = graphene.Schema(query=Query, mutation = Mutation)
