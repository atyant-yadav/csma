# Author: Atyant Yadav

BEGIN {
	dropped_pkts = 0;
}
($1 == "d") and ($4 != 0) {
	dropped_pkts++ ;
}
END {
    flow_start_time = 0.1; # configured in the tcl file;
    total_time_taken = time_of_last_reception -  flow_start_time ;
	print  dropped_pkts;
}
