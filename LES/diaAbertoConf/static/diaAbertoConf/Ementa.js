//----------------------------------------------------------------------
//                      Button Add and Remove logic 
//-----------------------------------------------------------------------
function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function cloneMore(selector, prefix) {
	var newElement = $(selector).clone(true);
	var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
	newElement.find('select,input,textarea').each(function() {
	
	    var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
		var id = $(this).attr('id').replace('-' + (total-1) + '-', '-' + total + '-');
		$(this).attr({'name': name, 'id': id}).val('');
	});
    
	total++;
	$('#id_' + prefix + '-TOTAL_FORMS').val(total);
	$(selector).after(newElement);
	var conditionRow = $('.prato-form-comp:not(:last)');
	conditionRow.find('.add-form-row').hide()
	conditionRow.find('.remove-form-row').show()
	return false;
}

function deleteForm(prefix, btn) {
	var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.prato-form-comp').remove();
        var forms = $('.prato-form-comp');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find('select').each(function() {
                updateElementIndex(this, prefix, i);
            })
            
            if(i+1 == forms.length){
				$(forms.get(i)).find(".add-form-row").show();
			}
        }
    }
    return false;
}

$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
	cloneMore('.prato-form-comp:last', 'form');
	return false;
})

$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
})

//============Modal===================//
$(function () {
    $('.delete').click(function (){
        var data_var = $(this).data('id');
        $("#deleteModal").attr("action", data_var);
    })
});
