$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Tipo_transporte')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("tipo_transporte")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("tipo_transporte")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Data')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("data")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("data")
            form.find("#id_direction").val("asc")
        }
    }else if($(this).hasClass('Origem')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("origem")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("origem")
            form.find("#id_direction").val("asc")
        }
	}else if($(this).hasClass('Destino')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("destino")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("destino")
            form.find("#id_direction").val("asc")
        }
    }else if($(this).hasClass('Horario')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("horarioid__hora_de_partida")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("horarioid__hora_de_partida")
            form.find("#id_direction").val("asc")
        }
	}
	
    form.submit()
})

$('button.page').click(function(){
    console.log("clicked")
    var page = $(this).data('page')
    var form = $('#formfilters')
    form.find("#id_page").val(page)
    form.submit()
})

$(document).ready( function(){
    $('th.Sortable').each(function(){
        $(this).has('i').addClass('tableBorder')
    })
})

$(".hide").hide();

$("table").click(function(event) {
	var target = $(event.target);
	if(!target.is('a')){
		if ( target.closest('tbody').find('i').hasClass('fas fa-chevron-right') ){
			target.closest('tbody').next().show();
			target.closest('tbody').find('i').removeClass();
			target.closest('tbody').find('i').addClass('fas fa-chevron-down');
		}else if( target.closest('tbody').find('i').hasClass('fas fa-chevron-down') ){
			target.closest('tbody').next().hide();
			target.closest('tbody').find('i').removeClass();
			target.closest('tbody').find('i').addClass('fas fa-chevron-right');	
			
		}    				
	}
})

$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})
