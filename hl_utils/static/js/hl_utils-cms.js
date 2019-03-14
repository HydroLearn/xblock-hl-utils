// helper methods for hl_utils
// Define mapping of tabs (modes) to display names
function HL_UTILS_STUDIO(xblock_element, options){


    this._element = xblock_element;
    this._highlight_class = "is_set"

    // this should be generated from passed studio buttons
    this.studio_buttons = {
        "editor": "EDITOR",
        "settings": "SETTINGS",
    };



    // add actions for the top of the modal to switch views
    for (var mode in this.studio_buttons) {

        $(this._element).closest('.modal-window').find('.editor-modes')
            .append(
                $('<li>', {class: "action-item"}).append(
                    $('<a />', {
                        //class: "action-primary",
                        class: mode + "-button modal_tab",
                        //id: mode,
                        text: studio_buttons[mode],
                        href: "#",
                        "data-mode":mode,
                    })
                )
            );
    }

    // map show/hide events for generated tabs
    $(this._element).closest('.modal-window').find('.editor-modes .modal_tab').click(function(){
        tab_switch($(this).attr('data-mode'));
    });

}
    // **********************************
    // modal tab switching methods
    // **********************************
    HL_UTILS_STUDIO.prototype.editor_toggle = function(){
        $('#learning_obj_creation', this._element).toggle()
        $('#learning_obj_listing', this._element).toggle()

        if($('#learning_obj_creation', this._element).is(':visible')){
            $(this._element).find('.save-button').addClass('disabled');
        }else{
            $(this._element).find('.save-button').removeClass('disabled');
        }
    }

    HL_UTILS_STUDIO.prototype.tab_highlight = function(toHighlight) {
        $(this._element).closest('.modal-window').find('.editor-modes .modal_tab').removeClass('is-set');
        $(this._element).closest('.modal-window').find('.editor-modes .modal_tab[data-mode="' + toHighlight + '"]').addClass('is-set');
    }

     HL_UTILS_STUDIO.prototype.tab_switch = function(toShow) {

        tab_highlight(toShow);

        $('.modal_tab_view', this._element).hide()
        $('.modal_tab_view[data-mode="' + toShow + '"]', this._element).show();

    }