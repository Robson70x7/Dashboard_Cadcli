(function(){
    $(document).ready(function () {
        //DataTable
        $('#client_table').DataTable({
            'paging'      : true,
            'lengthChange': false,
            'searching'   : false,
            'ordering'    : true,
            'info'        : true,
            'autoWidth'   : false
        });
    
        //Datemask dd/mm/yyyy
        $('input[datemask]').inputmask('dd/mm/yyyy', { 'placeholder': 'dd/mm/yyyy' });
        $('input[rg-mask]').inputmask('99.999.999.*', {'placeholder': '__.___.___-_'})
        $('input[cpf-mask]').inputmask('999.999.999-99', {'placeholder': '___.___.___-__'})
    });
});

