from django.shortcuts import render


def index(request):
    context = {
        'username': 'Турганов И.Д.',
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6_090.00,
             'image': 'Adidas-hoodie.png',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},

            {'name': 'Синяя куртка The North Face',
             'price': 23_725.00,
             'image': 'Blue-jacket-The-North-Face.png',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},

            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3_390.00,
             'image': 'Brown-sports-oversized-top-ASOS-DESIGN.png',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},

            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2_340.00,
             'image': 'Black-Nike-Heritage-backpack.png',
             'description': 'Плотная ткань. Легкий материал.'},

            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13_590.00,
             'image': 'Black-Dr-Martens-shoes.png',
             'description': 'Гладкий кожаный верх. Натуральный материал.'},

            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2_890.00,
             'image': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
        'title': 'GeekShop - Каталог',
    }
    return render(request, 'products/products.html', context)

