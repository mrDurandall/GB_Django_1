from django.contrib.auth.mixins import UserPassesTestMixin


class CommonContextMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IsStaffTestMixin(UserPassesTestMixin):

    def test_func(self):
        u = self.request.user
        return u.is_staff

