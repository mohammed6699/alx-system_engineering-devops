#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/School/).join
else
  puts "No ARGV Provided"
end
