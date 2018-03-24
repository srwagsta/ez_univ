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


class ValidateUnconnectedSectionsDeleteMixin:
    """This mixin must **only** be used with ``Instructor``, ``Course``, ``Semester``,
    and ``Student`` objects of the ``Courseinfo`` application due to it's
    required functions and fields. """
    failed_delete_template = None
    object = None
    template_name = None

    def get(self, request, *args, **kwargs):
        """Overrides the generic ``DeleteView`` :py:func: `get` to ensure that the
        ``Courseinfo`` object the is removed is not linked to any ``sections``. This preserves the
        database structure. """
        self.object = self.get_object()
        context = self.get_context_data()
        context['model_name'] = self.__class__.model.__name__
        context['page_title'] = 'Delete ' + context['model_name']
        context['list_url'] = 'courseinfo:' + context['model_name'].lower() + '_list'
        obj = self.get_object()
        if obj.sections.count() > 0:
            self.template_name = self.failed_delete_template
            context['sections'] = obj.sections.all()
            context['page_title'] = 'Error Deleting ' + context['model_name']
        return self.render_to_response(context)


class CourseActionMixin:
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(CourseActionMixin, self).form_valid(form)
