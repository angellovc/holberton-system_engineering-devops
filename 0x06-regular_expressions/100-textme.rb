#!/usr/bin/env ruby


from = ARGV[0].scan(/from:(.\w+)/).join
to = ARGV[0].scan(/to:([\w\+-]+)/).join
flags = ARGV[0].scan(/flags:([\w\+-:]+)/).join

puts "#{from},#{to},#{flags}"