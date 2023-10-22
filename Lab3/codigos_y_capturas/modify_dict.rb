#!/usr/bin/env ruby

File.open("rockyou.txt", :encoding => 'iso-8859-15') do |input_file|
  File.open("rockyou_mod.dic", "w") do |output_file|
    input_file.each_line do |line|
      if !line.match?(/\A\d/)
        output_file.puts line.capitalize.strip + '0'
      end
    end
  end
end
