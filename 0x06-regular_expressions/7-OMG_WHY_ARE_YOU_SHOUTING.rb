#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/[A-Z]+/).join
else
  puts "No ARGV Found"
end
