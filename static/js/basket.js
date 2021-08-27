window.onload = function (){
    $('.basket_window').on('click', 'input[type="number"]', function () {
        var target = event.target;
        console.log(target.name) ;
        console.log(target.value);

        $.ajax({
            url: '/basket/edit/' + target.name + '/' + target.value + '/',
            success: function (data) {
                $('.basket_window').html(data.result)
            },
        });
    });
}

