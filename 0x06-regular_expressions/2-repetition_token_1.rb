#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hb?tn/).join
else
  puts "NO ARGV Found"
end
