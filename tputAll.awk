# Author: Atyant Yadav

BEGIN {
	no_pkts = 0;
	total_data_received = 0;
	time_of_last_reception = 0;
}
($1 == "r") && ($4==0) {
	total_data_received += $6; 
	time_of_last_reception = $2; 
	no_pkts++ ;
}
END {
    flow_start_time = 0.1; # configured in the tcl file;
    total_time_taken = time_of_last_reception -  flow_start_time ;
	#print total_data_received, time_of_last_reception, no_pkts;
    #print "throughput =",  total_data_received*8/(total_time_taken*1000), "Kbps";
    print total_data_received*8/(total_time_taken*1000);
}
