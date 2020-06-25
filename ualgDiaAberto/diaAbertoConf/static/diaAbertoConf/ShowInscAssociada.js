$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Id')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("inscricaoid__id")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("inscricaoid__id")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Escola')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("inscricaoid__escolaid__nome")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("inscricaoid__escolaid__nome")
            form.find("#id_direction").val("asc")
        }
    }else if($(this).hasClass('Num_passageiros')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("num_passageiros")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("num_passageiros")
            form.find("#id_direction").val("asc")
        }
	}
	
    form.submit()
})

$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})

$(document).ready( function(){
    $('th.Sortable').each(function(){
        $(this).has('i').addClass('tableBorder')
    })
})

