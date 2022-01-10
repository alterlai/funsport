$(document).ready(function() {

    // DOM elementen met een link class worden gelinkt naar de URL in de data-target property.
    $('.link').click(function() {
        let url = $(this).data('target');
        window.location.href = url
    })
});