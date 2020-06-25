$('th.Sortable').click(function(){

    var form = $('#formfilters')

    if($(this).hasClass('Nome')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("nome")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("nome")
            form.find("#id_direction").val("asc")    
        }
    }else if($(this).hasClass('Email')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("email")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("email")
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