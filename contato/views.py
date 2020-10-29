from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
from .models import Message
from .forms import MessageForm

class MessageView(CreateView):
    model = Message
    fields = ('name', 'email', 'message')
    template_name = 'contato/index.html'

    def post(self, request, *args, **kwargs):
        form = MessageForm(data=request.POST)

        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect("contato:contato_index")

        return self.render_to_response({"form", form})
