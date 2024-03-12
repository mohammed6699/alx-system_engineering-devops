#!/usr/bin/env ruby
if ARGV[0]
  puts ARGV[0].scan(/hbt*n/).join
else
  puts "No ARGV Found"
end
