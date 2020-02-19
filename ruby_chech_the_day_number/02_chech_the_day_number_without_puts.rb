# the beginning of ....
puts 'Please enter the months day:'
day = gets.chomp.to_i
puts 'Please enter the month number:'
month = gets.chomp.to_i
puts 'Please enter the year:'
year = gets.chomp.to_i
puts "The date you entered: #{day}.#{month}.#{year}"

# method to chech is the year a leap year or not
def leap?(year)
  ((year % 4).zero? && year % 100 != 0) || (year % 400).zero?
end

# method to generate the hash "hash_number_days_in_months"
def getting_hash_number_days_in_months(year)
  days_amount_in_month = { 1 => 31, 2 => 28, 3 => 31, 4 => 30, 5 => 31, 6 => 30,
                           7 => 31, 8 => 31, 9 => 30, 10 => 31, 11 => 30, 12 => 31 }

  if leap?(year)
    days_amount_in_month[2] = 29
  end
  return days_amount_in_month
end

hash_number_days_in_months = getting_hash_number_days_in_months(year)

# method to calculate product "day_number_of_the_year"
def day_number_of_the_year(day, month, hash_number_days_in_months)
  var = 0
  if month > 1
    for i in 1...month
      var += hash_number_days_in_months[i]
    end
  end
  return var + day
end

puts "day_number_of_the_year: #{day_number_of_the_year(day, month, hash_number_days_in_months)}"
