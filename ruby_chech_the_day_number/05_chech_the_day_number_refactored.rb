# frozen_string_literal: true

# the beginning of ....
puts 'Please enter the months day:'
day = gets.chomp.to_i
puts 'Please enter the month number:'
month = gets.chomp.to_i
puts 'Please enter the year:'
year = gets.chomp.to_i

# method to chech is the year a leap year or not
def leap? year
  ((year % 4).zero? && year % 100 != 0) || (year % 400).zero?
end

# method to generate the hash "hash_number_of_days"
def hash_number_of_days year
  hash = { 1 => 31, 2 => 28, 3 => 31, 4 => 30, 5 => 31, 6 => 30,
           7 => 31, 8 => 31, 9 => 30, 10 => 31, 11 => 30, 12 => 31 }

  hash[2] = 29 if leap? year
  hash
end

# method to calculate the product: "day_number_of_the_year"
def day_number_of_the_year day, month, hash
  (1...month).each_with_index { |elem, index| if month > 1 then day += hash[index + 1] end }
  day
end

# print the output
puts "The date you entered: #{'%02d' % day}.#{'%02d' % month}.#{'%04d' % year}"
puts "That is the #{day_number_of_the_year(day, month, hash_number_of_days(year))}. day in #{year}. year."
