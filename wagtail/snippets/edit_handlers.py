from warnings import warn

from wagtail.admin.panels import FieldPanel
from wagtail.utils.deprecation import RemovedInWagtail219Warning


class SnippetChooserPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        warn(
            "wagtail.snippets.edit_handlers.SnippetChooserPanel is obsolete and should be replaced by wagtail.admin.panels.FieldPanel",
            category=RemovedInWagtail219Warning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)
