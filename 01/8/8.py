# TODO: non-existent index

product = 'Sony'
price = 85

# concatenation
print('Product: ' + product + ', Price: ' + str(price))

print('=' * 20)

# %
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
print('Product: %(product)s, Price: %(price).2f' % {'product': product, 'price': price})

print('=' * 20)

print('Product: %s, Price: %.2f' % (product, price))

print('=' * 20)

print(.1 + .2)
print('%.1f' % (.1 + .2))

print('=' * 20)

# format
print('Product: {}, Price: {:.2f}'.format(product, price))

print('=' * 20)

print('Product: {0}, Price: {1} Price2: {1:.2f}'.format(product, price))

print('=' * 20)

print('Product: {product}, Price: {price:.2f}'.format(product=product, price=price))

print('=' * 20)

# '%' Число умножается на 100, отображается число с плавающей точкой, а за ним знак %.
print('Product: {product}, Old price: {old_price}, New price: {new_price}, Discount: {discount:.2%}'.format(
    product=product, old_price=100, new_price=85, discount=(1 - 85 / 100)))
