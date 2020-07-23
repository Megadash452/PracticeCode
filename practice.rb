# Data types
	# Strings -> "hello"
	# Numbers -> (Integer, Float, BigDecimal)
	# Boolean -> true, false
	# Hashes -> {"hi" => "goodbye", 2 => "banan"}
	# Array ->  [1, 2]
	# Dictionary -> {}
	# Symbol -> :hello

	# Variables
	var = "this is a *variable*"
	greeting = "Hello!"
	puts greeting

	greeting = "Greetings, human."
	puts greeting
	# ctrl+/ to comment a highlight


# Methods
	def say_hello(name, num)
		puts "Greetings, #{name}."
		puts "you are number #{num}."
	end

	def assign(name, group)
		say_hello(name, 452)
		puts "You are in group #{group}."
	end

say_hello("Megadash", 452)
assign('Megadash', 2)

def even_or_odd(number)
	#to_i turns string to integer
	if number.to_i == 0 && number != 0
		puts "NOT A NUMBER!!1!1!!1!!"
	elsif number.to_i.even?
		puts "#{number} is even"
	else
		puts "#{number} is odd"
	end
end

even_or_odd("fsa")