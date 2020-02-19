# seed array
a = [4, 2, -1, 4, -55, 5, 5, -1, 7, 0, 1, 8, 46]

# output seed
puts("   seed: #{a}")

# bussines logic
product = a.each_with_index do |_, i|
	if i > 0 && i < a.size - 1
		if a[i].even?
			a[i] += a.first
		end
	end
end

# output product
puts("product: #{product}")
