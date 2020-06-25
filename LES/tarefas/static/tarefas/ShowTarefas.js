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
    }else if($(this).hasClass('Tipo')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("tipoTarefa")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("tipoTarefa")
            form.find("#id_direction").val("asc")
        }
    }else if($(this).hasClass('Estado')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("estado")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("estado")
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


$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})

$('.rmcolab').click(function (){
    var data_var = $(this).data('id');
    $("#removeColabModal").attr("action", data_var);
})


$(".expand").hide();

$("table").click(function(event) {
    //event.stopPropagation();
    var target = $(event.target);
    if(!target.is('a') && !target.is('button')){
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