"""
# Ruby

def fibonacci(n)
    if n < 3
        1
    else
        fibonacci(n - 1) + fibonacci(n - 2)
    end
end

(1..16).each {|n| puts "#{fibonacci(n)}, "}
puts "..."

"""

def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#for x in range(101):
#    fibonacci(x)

print("Import was succesfull")
