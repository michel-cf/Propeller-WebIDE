/**
 * Created by michel on 04/10/16.
 */

$(document).ready(function () {
    var main_editor = ace.edit("ace-main-editor");
    main_editor.setTheme("ace/theme/chrome");
    main_editor.getSession().setMode("ace/mode/c_cpp");

    var second_editor = ace.edit("ace-second-editor");
    second_editor.setTheme("ace/theme/chrome");
    second_editor.getSession().setMode("ace/mode/c_cpp");

    $('#project-file-tree').on('select_node.jstree', function (e, data) {
        document.location = data.node.a_attr.href;
  }).jstree({
        "core" : {
    "multiple" : false
  }
    });

    $('.sidebar-title').click(function() {
        var sidebar = $(this).parent();
        sidebar.toggleClass('collapsed');
        $('body').toggleClass(sidebar.attr('id'));
    });

    $('#compile-log .widget-title').click(function() {
        var compile_log = $('#compile-log');
        compile_log.toggleClass('collapsed');
    });

    if (screenfull.enabled) {
        $('#fullscreen').click(function (event) {
            event.preventDefault();
            screenfull.toggle();
            return false;
        }).removeClass('hidden');
    }

    resize();
});

function resize() {
    $("#editor").height($(window).height() - 100);
}

$( window ).resize(function() {
    resize();
});

resize();
