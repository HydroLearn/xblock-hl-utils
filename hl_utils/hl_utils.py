from web_fragments.fragment import Fragment

from xblockutils.resources import ResourceLoader
loader = ResourceLoader(__name__)


class HLXblockModalHelperMixin(object):
    """
        mixin to add modal tab definitions with associated templates
        to studio fragments
    """

    def get_modal_tabs(self):
        """
            expected to return list of tuples with
                - tab_display_name
                - rendered template
                - list of script/style resources (maybe?)

            :return:
        """

        return []

    def studio_view(self, context):

        context = context or {}
        context['modal_tabs'] = self.get_modal_tabs()

        fragment = super(HLXblockModalHelperMixin, self).studio_view(context)

        # add additional scripts/styling resources

        return fragment