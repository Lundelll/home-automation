from wtforms import widgets


# This custom widget is made to add list-group-item to the li tag... :@
class CustomListWidgetRemoveDevice(object):

    def __init__(self, html_tag='ul', prefix_label=False):
        assert html_tag in ('ol', 'ul')
        self.html_tag = html_tag
        self.prefix_label = prefix_label

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = ['<%s %s>' % (self.html_tag, widgets.html_params(**kwargs))]
        for subfield in field:
            if self.prefix_label:
                html.append('<li class="list-group-item">%s %s</li>' % (subfield.label, subfield()))
            else:
                html.append('<li class="list-group-item">%s %s</li>' % (subfield(), subfield.label))
        html.append('</%s>' % self.html_tag)
        return widgets.HTMLString(''.join(html))
