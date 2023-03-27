#include <iostream>
#include <time.h>
using namespace std;

struct timespec start, stop;

void start_clock(){
    clock_gettime(CLOCK_REALTIME, &start);
}
void stop_clock(){
    clock_gettime(CLOCK_REALTIME, &stop);
    cout << (stop.tv_sec - start.tv_sec) + (stop.tv_nsec - start.tv_nsec) / 1000000000.0;
}