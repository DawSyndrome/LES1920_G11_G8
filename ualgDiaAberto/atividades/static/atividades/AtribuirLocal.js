$('.imageShow').click(function (){
    var data_var = "/media/" + $(this).data('image');
    $("#ImageModal").find('img').attr("src", data_var);
})

$(document).on('click', '.show-indoor', function(){
    $('.indoor').show();
    $('.outdoor').hide();
    $('.hide-indoor').prop('required', false);
    $('.show-indoor').prop('required', true);
});
$(document).on('click', '.hide-indoor', function(){
    $('.indoor').hide();
    $('.outdoor').show();
    $('.hide-indoor').prop('required', true);
    $('.show-indoor').prop('required', false);
});

$(document).ready(function(){
    if  ($('.hide-indoor').is(':checked')){
        $('.indoor').hide();
        $('.outdoor').show();
        $('.hide-indoor').prop('required', true);
        $('.show-indoor').prop('required', false);

    }else if ($('.show-indoor').is(':checked')){
        $('.indoor').show();
        $('.outdoor').hide();
        $('.hide-indoor').prop('required', false);
        $('.show-indoor').prop('required', true);
    }
})

$('input[type=radio]').change(function(){
    if ($(this).val() == 'True'){
        getEdificio();
    }
    else{
        getLocalExterior();
    }
})

function getDescricao(){
    localid = $('select[name=localid_exterior]').val();
    request_url = '/GestaoAtividades/getDescricaoLocal/' + localid;
    $.ajax({
            url: request_url,
            dataType: "json",
            success: function(data){
                $.each(data, function(index, text){                  
                    $('textarea[name=descricao]').html(text)
                })
            },
        });
}

function getLocalImage(){
    $('a.imageShow').data("image", "")
    $('#mapa_sala').hide()
    console.log("hh")
    var localid

    if($('.show-indoor').is(':checked'))
        localid = $('select[name=localid_interior]').val();
    else if($('.hide-indoor').is(':checked'))
        localid = $('select[name=localid_exterior]').val();
    
    if (localid){
        $('#mapa_sala').show()

        request_url = '/GestaoAtividades/getLocalImage/' + localid;
        $.ajax({
                url: request_url,
                dataType: "json",
                success: function(data){
                    $.each(data, function(index, text){
                        console.log(text)
                        if(text != '')
                            $('a.imageShow').data("image", text)
                        else
                            $('#mapa_sala').hide()
                    })
                },
        }); 
    }
}

function getLocalExterior(){
    $('select[name=localid_exterior]').find('option').each(function(){
        $(this).remove();
    })
    $('textarea[name=descricao]').html('')
    campusid = $('select[name=campusid]').val();
    request_url = '/GestaoAtividades/getLocalExterior/' + campusid;
    $.ajax({
            url: request_url,
            dataType: "json",
            success: function(data){
                $.each(data, function(index, text){
                    $('select[name=localid_exterior]').append(
                        $('<option></option>').val(index).html(text)
                    )
                })
                getLocalImage();
                getDescricao();
            },
        });
}

function getLocais(){
    edificioid = $('select[name=edicifioid]').val();
    request_url = '/GestaoAtividades/getLocal/' + edificioid;
    $.ajax({
        url: request_url,
        dataType: "json",
        success: function(data){
            $.each(data, function(index, text){
                $('select[name=localid_interior]').append(
                    $('<option></option>').val(index).html(text)
                )
            })
            getLocalImage();
        },
    });
}

function getEdificio(){
     $('select[name=edicifioid]').find('option').each(function(){
        $(this).remove();
    })
    $('select[name=localid_interior]').find('option').each(function(){
        $(this).remove();
    })
    campusid = $('select[name=campusid]').val();
    console.log(campusid);
    request_url = '/GestaoAtividades/getEdificio/' + campusid;
    $.ajax({
        url: request_url,
        dataType: "json",
        success: function(data){
            $.each(data, function(index, text){
                $('select[name=edicifioid]').append(
                    $('<option></option>').val(index).html(text)
                )
            })
            getLocais()
        },
    });
}

$('select[name=campusid]').change(function(){
    if  ($('.hide-indoor').is(':checked')){       
        getLocalExterior();
    }else if ($('.show-indoor').is(':checked')){
        getEdificio();
    }
})

$('select[name=localid_exterior]').change(function(){
   getDescricao();
   getLocalImage()
})

$('select[name=localid_interior]').change(function(){
    getLocalImage()
 })

$('select[name=edicifioid]').change(function(){
    $('select[name=localid_interior]').find('option').each(function(){
        $(this).remove();
    })
    getLocais()
})