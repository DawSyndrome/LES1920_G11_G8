$('.save').hide()
$('.previousStep').attr("disabled", true)

currentStep = 1

$('.nextStep').click(function(){
    if( currentStep > 0 && currentStep < 5)
    currentStep++
    if(currentStep == 2){
        $('.InfoDiaAberto').hide()
        $('.InfoAtividades').show()
        $('.step1').addClass("bg-secondary") 
        $('.step2').removeClass("bg-secondary") 

        $('.previousStep').attr("disabled", false);
    }else if(currentStep == 3){
        $('.InfoAtividades').hide()
        $('.InfoInscricao').show()
        $('.step2').addClass("bg-secondary") 
        $('.step3').removeClass("bg-secondary") 
    }else if(currentStep == 4){
        $('.InfoInscricao').hide()
        $('.InfoAlmoços').show()
        $('.step3').addClass("bg-secondary") 
        $('.step4').removeClass("bg-secondary") 
    }else if(currentStep == 5){
        $('.InfoAlmoços').hide()
        $('.InfoContactos').show()
        $('.step4').addClass("bg-secondary") 
        $('.step5').removeClass("bg-secondary") 
        $('.save').show()

        $('.nextStep').attr("disabled", true);
    }
})

$('.previousStep').click(function(){
    if( currentStep > 1 && currentStep < 6){
        currentStep--
        if(currentStep == 1){
            $('.previousStep').attr("disabled", true);

            $('.InfoAtividades').hide()
            $('.InfoDiaAberto').show()
            $('.step2').addClass("bg-secondary") 
            $('.step1').removeClass("bg-secondary") 
        }else if(currentStep == 2){
            $('.InfoInscricao').hide()
            $('.InfoAtividades').show()
            $('.step3').addClass("bg-secondary") 
            $('.step2').removeClass("bg-secondary") 
        }else if(currentStep == 3){
            $('.InfoAlmoços').hide()
            $('.InfoInscricao').show()
            $('.step4').addClass("bg-secondary") 
            $('.step3').removeClass("bg-secondary") 
        }else if(currentStep == 4){
            $('.InfoContactos').hide()
            $('.InfoAlmoços').show()
            $('.step5').addClass("bg-secondary") 
            $('.step4').removeClass("bg-secondary") 
            $('.save').hide()

            $('.nextStep').attr("disabled", false);
        }
    }
})

function goToStep(step){
    
    console.log(step)
    $('.save').hide()
    if(step == 1){
        currentStep = 1
        $('.previousStep').attr("disabled", true);
        $('.nextStep').attr("disabled", false);

        $('.InfoDiaAberto').show()
        $('.InfoAtividades').hide()
        $('.InfoInscricao').hide()
        $('.InfoAlmoços').hide()
        $('.InfoContactos').hide()
        
        $('.step5').addClass("bg-secondary")
        $('.step4').addClass("bg-secondary") 
        $('.step3').addClass("bg-secondary") 
        $('.step2').addClass("bg-secondary")  


        $('.step1').removeClass("bg-secondary") 

    }else if(step == 2){
        currentStep = 2
        $('.previousStep').attr("disabled", false);
        $('.nextStep').attr("disabled", false);

        $('.InfoDiaAberto').hide()
        $('.InfoAtividades').show()
        $('.InfoInscricao').hide()
        $('.InfoAlmoços').hide()
        $('.InfoContactos').hide()
      
        $('.step5').addClass("bg-secondary") 
        $('.step4').addClass("bg-secondary") 
        $('.step3').addClass("bg-secondary") 
        $('.step1').addClass("bg-secondary")

        $('.step2').removeClass("bg-secondary")

    }else if(step == 3){
        currentStep = 3
        $('.previousStep').attr("disabled", false);
        $('.nextStep').attr("disabled", false);

        $('.InfoDiaAberto').hide()
        $('.InfoAtividades').hide()
        $('.InfoInscricao').show()
        $('.InfoAlmoços').hide()
        $('.InfoContactos').hide()
      
        
        $('.step5').addClass("bg-secondary") 
        $('.step4').addClass("bg-secondary") 
        $('.step2').addClass("bg-secondary") 
        $('.step1').addClass("bg-secondary")

        $('.step3').removeClass("bg-secondary") 

    }else if(step == 4){
        currentStep = 4
        $('.previousStep').attr("disabled", false);
        $('.nextStep').attr("disabled", false);

        $('.InfoDiaAberto').hide()
        $('.InfoAtividades').hide()
        $('.InfoInscricao').hide()
        $('.InfoAlmoços').show()
        $('.InfoContactos').hide()
      
        

        $('.step5').addClass("bg-secondary") 
        $('.step3').addClass("bg-secondary") 
        $('.step2').addClass("bg-secondary") 
        $('.step1').addClass("bg-secondary")

        $('.step4').removeClass("bg-secondary") 

    }

}
