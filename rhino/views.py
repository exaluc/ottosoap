from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Integer
from spyne.model.complex import Iterable
from spyne.service import Service
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoComplexModel
from rhino.models import Saisie


class LaSaisie(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = Saisie


class SaisieService(Service):
    @rpc(Integer, _returns=LaSaisie)
    def get_saisie(ctx, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise ResourceNotFoundError('LaSaisie')

    @rpc(Integer, _returns=Iterable(LaSaisie))
    def get_saisies(ctx, pk):
        try:
            return Note.objects.all()
        except Note.DoesNotExist:
            raise ResourceNotFoundError('LaSaisie')

    @rpc(LaSaisie, _returns=LaSaisie)
    def create_saisie(ctx, note):
        try:
            return Note.objects.create(**note.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError('LaSaisie')


app = Application([SaisieService],
                  'ottosoap.rhino',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11(),
                  )

saisie_soap_service = csrf_exempt(DjangoApplication(app))
