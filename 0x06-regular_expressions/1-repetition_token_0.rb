#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hbt{2,5}n/).join
else
  puts "No ARGV Found"
end
