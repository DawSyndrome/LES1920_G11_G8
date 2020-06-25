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
	newElement.find('select').each(function() {
	
	    var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
		var id = $(this).attr('id').replace('-' + (total-1) + '-', '-' + total + '-');
		$(this).attr({'name': name, 'id': id}).val('');
	});
    
	total++;
	$('#id_' + prefix + '-TOTAL_FORMS').val(total);
	$(selector).after(newElement);
	var conditionRow = $('.tarefaGrupo-form-comp:not(:last)');
	conditionRow.find('.add-form-row').hide()
	conditionRow.find('.remove-form-row').show()
	return false;
}

function deleteForm(prefix, btn) {
	var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.tarefaGrupo-form-comp').remove();
        var forms = $('.tarefaGrupo-form-comp');
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
	cloneMore('.tarefaGrupo-form-comp:last', 'form');
	return false;
})

$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
})

//-----------------------------------------------------------
//----------------------------------------------------------
//-----------------------------------------------------------
/*
function removeInsc(select){

    var value
    $(select).find('option').each(function(){
        console.log("aa")
    })
    $('select[name$=inscricao]').each(function(){
        if($(this).attr('id') != $(select).attr('id') && $(this).val()){
            value = $(this).val()
            $(select).find('option').each(function(){
                if ($(this).val == value)
                    $(this).hide()
            })
        }

    })
}

$('select[name$=inscricao]').change(function(){ 
    $('select[name$=inscricao]').each(function(){
        select = $(this)
        var value
        $('select[name$=inscricao]').each(function(){
            if($(this).attr('id') != select.attr('id') && $(this).val()){
                value = $(this).val()
                select.find('option').each(function(){
                    if ($(this).val == value)
                        $(this).hide()
                })
            }
    
        })
    })
})
*/
//----------------------------------------------------
//                  AJAX 
//----------------------------------------------------
function cleanForm(){
    $('.TarefaTransporte').find('select').each(function(){
        if(!$(this).is('select[name=dia]')){
            $(this).find('option').each(function(){
                $(this).remove();
            })
        }
    })
    $('.TarefaTransporte').find('input[name=horario]').val('');		
    $('.TarefaTransporte').find('input[name=destino]').val('');		
    $('.TarefaTransporte').find('input[name=origem]').val('');	

}

function addGrupos(){

    $('.tarefaGrupo-form-comp:not(:first)').remove()
    $('.tarefaGrupo-form-comp').find(".add-form-row").show();
    $('select[name$=inscricao]').find('option').each(function(){
        $(this).remove();
    })
    $('input[name$=form-TOTAL_FORMS]').val(1)
    

    if ($('select[name=sessaoAtividade_destino]').val()){
        sessaoAtividade_origem = $('select[name=sessaoAtividade_origem]').val();
        sessaoAtividade_destino = $('select[name=sessaoAtividade_destino]').val();
        dia = $('select[name=dia]').val();
        request_url = '/Tarefas/getGrupos/' + sessaoAtividade_origem + '/' + sessaoAtividade_destino + '/' + dia;
        console.log(sessaoAtividade_origem + "->" + sessaoAtividade_destino)

        $.ajax({
            url: request_url,
            dataType: "json",
            success: function(data){
                $.each(data, function(index, text){
                    $('select[name$=inscricao]').append(
                        $('<option></option>').val(index).html(text)
                    )
                })
            }
        })
    }
}

function addLocal(prefix){
    if( $('select[name=sessaoAtividade_' + prefix +']').val()){
        sessao_atividadeid = $('select[name=sessaoAtividade_' + prefix +']').val();
        request_url = '/Tarefas/getLocal_Sessao/' + sessao_atividadeid

        $.ajax({
            url: request_url,
            dataType: "json",
            success: function(data){
                $.each(data, function(index, text){
                    $('input[name=' + prefix +']').val(text)
                })
            }
        })
    }else
        $('input[name=' + prefix +']').val('');
}

function addProximaAtividade(){
    if( $('select[name=sessaoAtividade_origem').val()){
        
        $('select[name=sessaoAtividade_destino]').find('option').each(function(){
            $(this).remove();
        })

        atividade_original = $('select[name=sessaoAtividade_origem]').val();
        date = $('select[name=dia]').val();
        request_url ='/Tarefas/getSessoesNext/'+ atividade_original + '/' + date;
        
        $.ajax({
            url: request_url,
            dataType: "json",
            success: function(data){
                $.each(data, function(text, index){
                    $('select[name=sessaoAtividade_destino]').append(
                        $('<option></option>').val(index).html(text)
                    )
                })
                addLocal('destino')
                addGrupos();
            },
        });

    }
}

function addHora(){
    if($('select[name=sessaoAtividade_origem]').val()){
        atividade_original = $('select[name=sessaoAtividade_origem]').val();
        request_url='/Tarefas/getHoraFim/' + atividade_original;

        $.ajax({
            url: request_url,
            dataType:"json",
            success: function(data){
                $.each(data, function(index, text){
                    $('input[name=horario]').val(text)
                })
            }
        })
    }
    
}

function addAtividadeAtual(){
    cleanForm();

    date = $('select[name=dia]').val();
    console.log(date)
    if(date){
        request_url = '/Tarefas/getSessoesByDate/' + date;
        
        $.ajax({
            url: request_url,
            dataType:"json",
            success: function(data){
                console.log(data)
                $.each(data, function(text, index){
                    $('select[name=sessaoAtividade_origem]').append(
                        $('<option></option>').val(index).html(text)
                    )
                })
                addLocal('origem');
                addProximaAtividade();
                addHora();
            }
        });
    }
}

$('select[name=dia]').change(function(){
    addAtividadeAtual()
})


$('select[name=sessaoAtividade_origem]').change(function(){
    addLocal('origem');
    addProximaAtividade();
    addHora();
    //addGrupos();
})

$('select[name=sessaoAtividade_destino]').change(function(){
    addLocal('destino');
    addGrupos();
})

$('select[name=atividade]').change(function(){

    $('select[name=sessaoAtividade]').find('option').each(function(){
        $(this).remove();
    })

    Atividadeid = $(this).val();
    request_url = '/Tarefas/getSessoes/' + Atividadeid;
    $.ajax({
        url: request_url,
        dataType: "json",
        success: function(data){
            $.each(data, function(text, index){
                $('select[name=sessaoAtividade]').append(
                    $('<option></option>').val(index).html(text)
                )
            })
        },
    });
})

//--------------------------------------------------------------------------

$('input[name=tipoTarefa').change(function(){
    if($(this).val() == 'Atividade'){
        $('.TarefaAtividade').show();
        $('.TarefaTransporte').hide();

        $('.tarefaGrupo-form-comp:not(:first)').remove()
        $('.tarefaGrupo-form-comp').find(".add-form-row").show();

        //Turns fields in Tarefa Atividade into required fields
        $('.TarefaAtividade').find('select').each(function(){
            $(this).prop('required', true)
        })

        $('.TarefaTransporte').find('input, select').each(function(){
            //Removes required atribute from fields in Tarefa Transporte
            if(!$(this).is('input[name$=_FORMS]') && $(this).is('input, select'))
                $(this).prop('required', false)

            if($(this).is('input[name$=form-TOTAL_FORMS]'))
                $(this).val(1)
            
            if(!$(this).is('input[name$=_FORMS]') && !$(this).is('select[name=dia]'))
                $(this).val('');
                         
            if($(this).is('select') && !$(this).is('select[name=dia]')){
                $(this).find('option').each(function(){
                    $(this).remove();
                })
            }
        })
    }else{
        $('.TarefaTransporte').show();
        addAtividadeAtual()
        $('.TarefaTransporte').find('input, select').each(function(){
            //Turns fields in Tarefa Transporte into required fields
            if(!$(this).is('input[name$=_FORMS]') && $(this).is('input, select'))
                $(this).prop('required', true)
        })

        $('.TarefaAtividade').hide();
        //Removes required atribute from fields in Tarefa Atividade
        $('.TarefaAtividade').find('select').each(function(){
            $(this).prop('required', false)
        })
    }
})

