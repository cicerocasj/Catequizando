# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["id"] = id
        context["title"] = u'Campanha da fraternidade'
        context["content"] = '''
João 1 ,14-23. Nossa vida é feita de tempo, e o tempo é uma dádiva de Deus, então é importante que seja usado em ações boas e frutíferas.” As atividades citadas por Francisco como fúteis são: “bater papo na internet ou com smartphones, assistir novelas na TV e [usar] os produtos do progresso tecnológico, que deveriam simplificar e melhorar a qualidade de vida, mas desviam a atenção do que é realmente importante”. O papa, de 77 anos, tem contas no Twitter em várias línguas '''
        context["objetive"] = '''
Apresentar para os catequizandos o tema da campanha da fraternindade. Explicar... '''
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/encontro.html')