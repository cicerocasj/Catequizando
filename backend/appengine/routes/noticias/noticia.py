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
        context["title"] = u'Papa fala com os jovens'
        context["content"] = '''
        O papa Francisco exortou 50 mil coroinhas alemães nesta terça-feira (5) a não perder tempo com internet, smartphones e televisão, mas dedicá-lo a atividades mais produtivas.
“Talvez muitos jovens percam horas demais com coisas fúteis”, declarou o pontífice em um discurso breve aos auxiliares de culto que peregrinaram a Roma, na Itália.
“Nossa vida é feita de tempo, e o tempo é uma dádiva de Deus, então é importante que seja usado em ações boas e frutíferas.”
As atividades citadas por Francisco como fúteis são: “bater papo na internet ou com smartphones, assistir novelas na TV e [usar] os produtos do progresso tecnológico, que deveriam simplificar e melhorar a qualidade de vida, mas desviam a atenção do que é realmente importante”.
O papa, de 77 anos, tem contas no Twitter em várias línguas. A rede social foi usada pela primeira vez em 2011 pelo antecessor de Francisco, Bento 16. A conta em inglês do Papa tem 4,3 milhões de seguidores. Seguem o perfil em português do pontífice 1,1 milhão de usuários.
Ele também descreveu a internet como “uma dádiva de Deus”, mas alertou que o mundo de alta velocidade das mídias sociais precisa de calma, reflexão e ternura para ser “uma rede não de cabos, mas de pessoas”
        '''
        context["link"] = u'http://g1.globo.com/tecnologia/noticia/2014/08/papa-fala-para-jovens-nao-perderem-tempo-com-internet-e-smartphones.html'
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/noticia.html')