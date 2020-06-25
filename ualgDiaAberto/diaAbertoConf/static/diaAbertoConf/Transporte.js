function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function cloneMore(selector, prefix) {
	var newElement = $(selector).clone(true);
	var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
	newElement.find('input, ul, select').each(function() {
	
		//if($(this).is('input'))
		if(!$(this).parent().is(".selectBox")){
			if(!$(this).is('ul'))
	    		var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
			var id = $(this).attr('id').replace('-' + (total-1) + '-', '-' + total + '-');

			if($(this).attr('type') === "checkbox"){
				$(this).attr({'name': name, 'id': id}).prop('checked', false);
			}else {
				$(this).attr({'name': name, 'id': id}).val('');
			}	
		}
		
	});
	newElement.find('label').each(function() {
	    var forValue = $(this).attr('for');
	    if (forValue) {
	      forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
	      $(this).attr({'for': forValue});
	    }
    })
    
	total++;
	$('#id_' + prefix + '-TOTAL_FORMS').val(total);
	newElement.find('#checkboxes').hide();
	
	//Removes error message so it doesnt appear in the new form
	newElement.find('.alert-danger').remove()
	
	$(selector).after(newElement);
	var conditionRow = $('.rota-form-comp:not(:last)');
	conditionRow.find('.add-form-row').hide()
	conditionRow.find('.remove-form-row').show()
	/*.removeClass('btn-outline-success').addClass('btn-outline-danger')
	.removeClass('add-form-row').addClass('remove-form-row')
	.html('Remover Rota');*/
	return false;
}

function deleteForm(prefix, btn) {
	var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.rota-form-comp').remove();
        var forms = $('.rota-form-comp');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find('input, ul, label').each(function() {
                updateElementIndex(this, prefix, i);
            })
            
            if(i+1 == forms.length){
				//console.log("hi")
				$(forms.get(i)).find(".add-form-row").show();
			}
        }
    }
    return false;
}

function showHorarios(horarios, dateVal){
	var checkedHorarios = [];
	$('.checkboxes').find('input').each(function() {
		if($(this).parents('.rota-form-comp').find('.date-Set').val() == dateVal && $(this).prop("checked")){
			checkedHorarios.push(this);
		}
	});
	horarios.each(function() {
		var currentHorario = $(this);
		if( checkedHorarios.length != 0){
			for(var i = 0; i < checkedHorarios.length; i++){
				if($(currentHorario).val() == $(checkedHorarios[i]).val() && $(currentHorario).attr('id') != $(checkedHorarios[i]).attr('id')) {
					//console.log("Hide " + $(checkedHorarios[i]).val() + " = " + $(currentHorario).val());
					currentHorario.parents("li").hide();
					break;
				}else {
					//console.log("Show " + $(checkedHorarios[i]).val() + " != " + $(currentHorario).val());
					currentHorario.parents("li").show();
				}
			}
		} else {
			currentHorario.parents("li").show();
		}
		
	})
}

function updateHorarios(){
	$('.checkboxes').each(function(){
		var dateVal = $(this).parents('.rota-form-comp').find('.date-Set').val();
		var horarios = $(this).find('input');
		showHorarios(horarios, dateVal);
	});
}

$(document).on('click', '.add-form-row', function(e){
	e.preventDefault();
	cloneMore('.rota-form-comp:last', 'form');
	return false;
});

$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
	updateHorarios();
    return false;
});


$(document).on('click', '.selectBox', function(){
	var checkboxes = $(this).nextAll('#checkboxes').first();
	var dateVal = $(this).parents('.rota-form-comp').find('.date-Set').val();
	var horarios = checkboxes.find('input');
	if(checkboxes.is(':hidden') && dateVal != null){
		console.log("show");
		checkboxes.show();
		showHorarios(horarios, dateVal);
	}else {
		console.log("hide");
		checkboxes.hide();
	}
})

$(document).on('click', 'li', function(){
	updateHorarios();
})

$('.date-Set').change(function(){
	$(this).parents('.rota-form-comp').find('input[type="checkbox"]').each(function(){
		$(this).prop('checked', false);
	})
	updateHorarios();
})