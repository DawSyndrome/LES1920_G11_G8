$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Id')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("id")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("id")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Escola')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("escolaid__nome")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("escolaid__nome")
            form.find("#id_direction").val("asc")
        }
    }
	
    form.submit()
})

$('button.page').click(function(){
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