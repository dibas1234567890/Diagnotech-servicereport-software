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


from django import template
import base64

register = template.Library()

@register.filter
def signature_base64_filter(signature):
    if signature:
        return f"data:image/png;base64,{base64.b64encode(signature).decode('utf-8')}"
    else:
        return ""
