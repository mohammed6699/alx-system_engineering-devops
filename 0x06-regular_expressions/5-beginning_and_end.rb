#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/^h.n$/).join
else
  puts "NO ARGV Found"
end
