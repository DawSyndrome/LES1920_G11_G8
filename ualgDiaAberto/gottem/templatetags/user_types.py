
from ..models import Utilizador

from django import template

register = template.Library()

@register.filter
def is_admin(value):
    return (value & int(Utilizador.USER_TYPES.Administrador)) != 0
@register.filter
def is_participante(value):
    return (value & int(Utilizador.USER_TYPES.Participante)) != 0
@register.filter
def is_docente(value):
    return (value & int(Utilizador.USER_TYPES.Docente)) != 0
@register.filter
def is_colaborador(value):
    return (value & int(Utilizador.USER_TYPES.Colaborador)) != 0
@register.filter
def is_coordenador(value):
    return (value & int(Utilizador.USER_TYPES.Coordenador)) != 0