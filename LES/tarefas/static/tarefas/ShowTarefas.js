$('th.Sortable').click(function(){
    if($(this).hasClass('Nome')){
        if($(this).hasClass('asc'))
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=nome&direction=desc"
        else
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=nome&direction=asc"
    }else if($(this).hasClass('Tipo')){
        if($(this).hasClass('asc'))
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=tipoTarefa&direction=desc"
        else
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=tipoTarefa&direction=asc"
    }else if($(this).hasClass('Estado')){
        if($(this).hasClass('asc'))
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=estado&direction=desc"
        else
            window.location.href =  "?page=" + $('span.current').html() + "&order_by=estado&direction=asc"
    }
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