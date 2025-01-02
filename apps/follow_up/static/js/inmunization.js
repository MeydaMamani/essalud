
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

$('#demo-input-search2').on('input', function(e) {
    e.preventDefault();
    addrow3.trigger('footable_filter', { filter: $(this).val() });
});
var addrow3 = $('#demo-foo-addrow2');
addrow3.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow3.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});


$('#demo-input-search3').on('input', function(e) {
    e.preventDefault();
    addrow3.trigger('footable_filter', { filter: $(this).val() });
});
var addrow3 = $('#demo-foo-addrow3');
addrow3.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$('#demo-input-search4').on('input', function(e) {
    e.preventDefault();
    addrow4.trigger('footable_filter', { filter: $(this).val() });
});
var addrow4 = $('#demo-foo-addrow4');
addrow4.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$('#demo-input-search5').on('input', function(e) {
    e.preventDefault();
    addrow5.trigger('footable_filter', { filter: $(this).val() });
});
var addrow5 = $('#demo-foo-addrow5');
addrow5.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$('#demo-input-search6').on('input', function(e) {
    e.preventDefault();
    addrow6.trigger('footable_filter', { filter: $(this).val() });
});
var addrow6 = $('#demo-foo-addrow6');
addrow6.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$('#demo-input-search7').on('input', function(e) {
    e.preventDefault();
    addrow7.trigger('footable_filter', { filter: $(this).val() });
});
var addrow7 = $('#demo-foo-addrow7');
addrow7.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});
