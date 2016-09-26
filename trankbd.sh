perl -p -i -e "s/<kbd[^>]+>|<\/kbd>/\`/g"  $*
perl -p -i -e "s/’/'/g"  $*
perl -p -i -e "s/‘/'/g"  $*
perl -p -i -e "s/¨//g"  $*
perl -p -i -e "s/°//g" $*
perl -p -i -e "s/ﬀ/ff/g"  $*
perl -p -i -e "s/ﬁ/fi/g"  $*
perl -p -i -e "s/ﬃ/ffi/g" $*
perl -p -i -e "s/ﬂ/fl/g" $*
perl -p -i -e "s/°//g" $*
perl -p -i -e "s//0/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//1/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//2/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//3/g"  $*
perl -p -i -e "s//4/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//5/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//6/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//7/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//8/g"  $*   #ef 9cf3  3  => f733
perl -p -i -e "s//9/g"  $*   #ef 9cf3  3  => f733
#perl -p -i -e "s//c/g"  $*   #ef 9da3  c  => 1110 1111 1001 1101 1010 0011  => f 0111 0110 0011 => f763
#perl -p -i -e "s//c/g"  $*   #ef 9da3  c  => 1110 1111 1001 1101 1010 0011  => f 0111 0110 0011 => f763

perl -p -i -e "s/–|—/-/g"  $*
perl -p -i -e "s/“|”/\"/g"  $*

#c3p7 => 

#(dotimes (n 26)
#  (insert-string "perl -p -i -e \"s/")
#  (insert-char (+ #xf761 n))
#  (insert-string "/")
#  (insert-char (+ #x41 n))
#  (insert-string "/g\" $*")
#  (insert-string "\n"))
#  
perl -p -i -e "s//A/g" $*
perl -p -i -e "s//B/g" $*
perl -p -i -e "s//C/g" $*
perl -p -i -e "s//D/g" $*
perl -p -i -e "s//E/g" $*
perl -p -i -e "s//F/g" $*
perl -p -i -e "s//G/g" $*
perl -p -i -e "s//H/g" $*
perl -p -i -e "s//I/g" $*
perl -p -i -e "s//J/g" $*
perl -p -i -e "s//K/g" $*
perl -p -i -e "s//L/g" $*
perl -p -i -e "s//M/g" $*
perl -p -i -e "s//N/g" $*
perl -p -i -e "s//O/g" $*
perl -p -i -e "s//P/g" $*
perl -p -i -e "s//Q/g" $*
perl -p -i -e "s//R/g" $*
perl -p -i -e "s//S/g" $*
perl -p -i -e "s//T/g" $*
perl -p -i -e "s//U/g" $*
perl -p -i -e "s//V/g" $*
perl -p -i -e "s//W/g" $*
perl -p -i -e "s//X/g" $*
perl -p -i -e "s//Y/g" $*
perl -p -i -e "s//Z/g" $*


#c397 => 1100 0011 1001 0111 => 000 1101 0111 => d7

perl -p -i -e "s/×/x/g" $*

perl -p -i -e "s/−/-/g" $*


