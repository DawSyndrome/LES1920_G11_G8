$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Hora_de_partida')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("hora_de_partida")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("hora_de_partida")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Hora_de_chegada')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("hora_de_chegada")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("hora_de_chegada")
            form.find("#id_direction").val("asc")
        }
    }
	
    form.submit()
})

$(document).ready( function(){
    $('th.Sortable').each(function(){
        $(this).has('i').addClass('tableBorder')
    })
})

$('button.page').click(function(){
    console.log("clicked")
    var page = $(this).data('page')
    var form = $('#formfilters')
    form.find("#id_page").val(page)
    form.submit()
})