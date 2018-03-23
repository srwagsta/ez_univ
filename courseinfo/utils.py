from django.shortcuts import redirect, render
from django.contrib import messages


class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})


class CourseActionMixin:
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(CourseActionMixin, self).form_valid(form)
