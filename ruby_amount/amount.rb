h = {}
sum_of_products = 0
user_input = nil
# A cycle is used to enter product parameters
# after entering each parameter (Product Name, Cost, Quantity)
# press "Enter" to go to the input of the next parameter.
# after entering 3 parameters - the loop asks if you want to continue entering?
# if yes then press "Enter" if not write in the line 'stop'.
puts 'Please enter product details (Name, Cost, Quantity)'
while user_input != 'stop'
  puts 'Please enter a product name:'
  product = gets.chomp
  puts 'Please enter the price of the goods:'
  unit_price = gets.chomp.to_i
  puts 'Please enter the quantity of goods:'
  quantity_of_goods = gets.chomp.to_f
  puts 'If there are no more products, enter “stop”, if there is, press “Enter”'
  user_input = gets.chomp
  h[product] = { unit_price: unit_price, quantity_of_goods: quantity_of_goods }
end
puts "Cart with goods: #{h}"
h.each do |name, value|
  print "The total amount for the product: #{name} - "
  puts total = (value[:unit_price] * value[:quantity_of_goods])
  sum_of_products += total
end
puts "The total amount of all products in the basket: #{sum_of_products}"