
$(document).ready(function () {
    //DataTable
    $('#client_table').DataTable({
        'select':true
    });   
    //Datemask dd/mm/yyyy
    $('input[datemask]').inputmask('dd/mm/yyyy', { 'placeholder': '__/__/____' });
    $('input[rg-mask]').inputmask('99.999.999.*', {'placeholder': '__.___.___-_'})
    $('input[cpf-mask]').inputmask('999.999.999-99', {'placeholder': '___.___.___-__'})
});

