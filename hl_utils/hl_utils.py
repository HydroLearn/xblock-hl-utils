from web_fragments.fragment import Fragment

from xblockutils.resources import ResourceLoader
loader = ResourceLoader(__name__)



# currently UNUSED until better implemented
class StudioModalFixMixin(object):

    def studio_view(self, context=None):
        """
            The studio view of the xblock

            return: a web fragment containing the necessary styles/scripts/templates
                for rendering the xblock editor in the cms xblock modal window.


        """
        # THIS TECHINCALLY CAN HAPPEN AS A MIXIN (expected to just do, not inherit)
        # fragment = super(StudioModalFixMixin, self).studio_view(context)
        fragment = Fragment()

        # add in the styling/script corrections for HL xblock component modals
        fragment.add_css(loader.load_unicode('static/css/modal-styling.css'))
        fragment.add_javascript(loader.load_unicode('static/js/StudioModalFix.js'))

        fragment.initialize_js('StudioModalFix_script')

        return fragment


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