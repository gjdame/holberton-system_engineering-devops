#!/usr/bin/env ruby
my_string = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/).join(" ")
my_string = my_string.squeeze(' ')
my_list = my_string.split
puts my_list.join(',')
