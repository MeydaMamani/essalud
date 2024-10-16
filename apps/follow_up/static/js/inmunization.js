$('#demo-input-search').on('input', function(e) {
    e.preventDefault();
    addrow2.trigger('footable_filter', { filter: $(this).val() });
});
var addrow2 = $('#demo-foo-addrow');
addrow2.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$("#search").click();