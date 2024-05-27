from django import template
from django.urls import reverse


register = template.Library()

@register.simple_tag(takes_context=True)
def check_client(context):
    user = context['user']
    if user.profile.client:
        return """<p class="h3">Clients are only allowed to report problems ! Please go here</p>
        <a href="{% url 'problem' %}"><button>
        Go To Client Page 
        </button></a>""".format(reverse('problem'))
    return ''
