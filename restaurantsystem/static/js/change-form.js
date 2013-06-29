
$(document).ready(function(){

    $('#id_product').change(function(){
        val = $('#id_product').find(":selected").attr('value');
        if (val != "")
        {
            $.ajax({
                url:'http://localhost:8000/admin/restaurantsystem/getupdatedprice/'+val+'/',
                dataType:'json'
            }).always(function( data, textStatus, jqXHR) {
                    $('#id_unit_price').attr('value', data.price);
                });

        }
        else
        {
            $('#id_unit_price').attr('value', '');
        }
    });

   /*$('#leke').click(function(e){
       e.preventDefault();
       alert('LEKE');
   });*/

});
