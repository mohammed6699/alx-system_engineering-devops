#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/^[0-9]{10}$/).join
else
  puts "No ARGV Found"
end
