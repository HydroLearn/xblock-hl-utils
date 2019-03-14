import json

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


class HLXBlockModalHelperMixin(object):
    """
        mixin to add modal tab definitions with associated templates
        to studio fragments
    """

    modal_tabs = []

    def get_modal_tabs(self):
        return self.modal_tabs

    def studio_view(self, context):

        context = context or {}
        context['modal_tabs'] = json.dumps(self.get_modal_tabs())
        context['num_tabs'] = len(self.get_modal_tabs())
        # fragment = super(HLXBlockModalHelperMixin, self).studio_view(context)

        fragment = Fragment()

        # add additional scripts/styling resources
        fragment.add_javascript(loader.load_unicode('static/js/hl_utils-cms.js'))
        fragment.add_css(loader.load_unicode('static/css/modal-styling.css'))

        return fragment