$(document).ready(function() {
    $('.date-mask').mask('00/00/0000');
    $('.date-mask-placeholder').mask('00/00/0000', {placeholder: "__/__/____"});
    $('.phone-mask').mask('(00) 0000-0000');    
    $('.cel-phone-mask').mask('(00) 0 0000-0000');    
    $('.cpf-mask').mask('000.000.000-00');    
    $('.cnpj-mask').mask('00.000.000/0000-00');    
    $('.datepicker').datepicker({
        dateFormat: "dd/mm/yy",
    });
});

$(document).ready(function() {
    $(window).keydown(function(event){
        if(event.keyCode == 13) {
        event.preventDefault();
        return false;
        }
    });
});


