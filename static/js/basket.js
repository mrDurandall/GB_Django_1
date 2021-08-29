window.onload = function (){
    $('.basket_window').on('click', 'input[type="number"]', function () {
        var target = event.target;

        $.ajax({
            url: '/basket/edit/' + target.name + '/' + target.value + '/',
            success: function (data) {
                $('.basket_window').html(data.result)
            },
        });
    });

    $('.basket_window').on('click', 'i', function () {
        var target = event.target;

        $.ajax({
            url: '/basket/remove/' + target.id + '/',
            success: function (data) {
                $('.basket_window').html(data.result)
            },
        });
    });

    $('.card').on('click', 'div[class="btn btn-outline-success"]', function () {
       var target = event.target;
       console.log('test');
       console.log(target.id)

       $.ajax({
           url: '/basket/add/' + target.id + '/',
       });
    });
}

