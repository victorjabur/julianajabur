from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from julianajaburapp.models import Choice, Poll

def handle_error500(request, template_name='error/500.html'):
    return render_to_response(template_name, context_instance = RequestContext(request))

def handle_error404(request, template_name='error/404.html'):
    return render_to_response(template_name, context_instance = RequestContext(request))

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    #t = loader.get_template('polls/index.html')
    #c = Context({
    #    'latest_poll_list': latest_poll_list,
    #})
    #return HttpResponse(t.render(c))

    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},
                               context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('julianajaburapp.views.results', args=(p.id,)))