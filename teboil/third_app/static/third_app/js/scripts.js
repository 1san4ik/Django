$(document).ready(function(){
    var form = $('#product-actions');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#quantity').val();
        console.log(nmb);

        var submit_btn = $('#add-to-cart');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("product_name");
        var price = submit_btn.data("product_price");
        console.log(product_id);
        console.log(name);
        console.log(price);
    })

});
