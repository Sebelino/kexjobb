set terminal pngcairo enhanced
set output "output.png"
set title "Power usage over time"
set xlabel "Time (seconds)"
set ylabel "Power ({/Symbol m}W)"
set nokey
set grid
plot [0:7200] [0:24000000] 'statistics.dat'
