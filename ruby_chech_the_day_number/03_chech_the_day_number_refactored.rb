# the beginning of ....
puts 'Please enter the months day:'
day = gets.chomp.to_i
puts 'Please enter the month number:'
month = gets.chomp.to_i
puts 'Please enter the year:'
year = gets.chomp.to_i

# method to chech is the year a leap year or not
def leap?(x)
  ((x % 4).zero? && x % 100 != 0) || (x % 400).zero?
end

# method to generate the hash "hash_number_days_in_months"
def getting_hash_number_days_in_months(x)
  h = { 1 => 31, 2 => 28, 3 => 31, 4 => 30, 5 => 31, 6 => 30,
        7 => 31, 8 => 31, 9 => 30, 10 => 31, 11 => 30, 12 => 31 }

  if leap?(x)
    h[2] = 29
  end
  return h
end

# method to calculate the product: "day_number_of_the_year"
def day_number_of_the_year(x, y, z)
  v = 0
  if y > 1
    for i in 1...y
      v += z[i]
    end
  end
  return v + x
end

puts "The date you entered: #{"%02d" % day}.#{"%02d" % month}.#{year}"
puts "That is the #{day_number_of_the_year(day, month, getting_hash_number_days_in_months(year))}. day in #{year}. year."
