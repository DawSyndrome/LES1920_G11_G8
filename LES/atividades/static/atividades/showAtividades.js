$('.delete').click(function (){
    var data_var = $(this).data('id');
    $("#deleteModal").attr("action", data_var);
})

$('.imageShow').click(function (){
    var data_var = "/media/" + $(this).data('image');
    $("#ImageModal").find('img').attr("src", data_var);
})

$('.recuse').click(function (){
    var data_var = $(this).data('id');
    $("#recuseModal").attr("action", data_var);
    console.log($(this).data('id'));
})

$('#id_localcampus').change(function(){
    $('select[name=localedicifio]').find('option').each(function(){
        $(this).remove();
    })

    campusid = $(this).val();
    request_url = '/GestaoAtividades/getEdificioCampus/' + campusid;
    $.ajax({
        url: request_url,
        dataType: "json",
        success: function(data){
            $('select[name=localedicifio]').append(
                $('<option></option>').html("Pesquisar por Edifício").attr('disabled', 'disabled').attr('selected', 'selected')
            )
            $.each(data, function(index, text){
                $('select[name=localedicifio]').append(
                    $('<option></option>').val(index).html(text)
                )
            })
        },
    });
})

/*$(".clickable-row").on('click', function(event) {
event.stopPropagation();
var target = $(event.target);
if(!target.is('a'))
    window.location = $(this).data("href");
});*/

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
    }
    else if($(this).hasClass('Tipo')){
        if($(this).hasClass('asc')){
            form.find("#id_order_by").val("tipo_atividade")
            form.find("#id_direction").val("desc")
        }else{
            form.find("#id_order_by").val("tipo_atividade")
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

