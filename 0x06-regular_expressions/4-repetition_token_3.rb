#!/usr/bin/env ruby
if ARGV.empty?
  puts "Please provide an argument."
else
  puts ARGV[0].scan(/^(?!.*hbon$|.*hbbn$).*$/)
end
