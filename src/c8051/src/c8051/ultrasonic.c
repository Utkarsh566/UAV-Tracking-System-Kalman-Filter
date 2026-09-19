#include "ultrasonic.h"

void Ultrasonic_Init(void)
{
    /* Configure trigger as output and echo as input. */
}

float Ultrasonic_ReadDistanceCm(void)
{
    /*
     * Typical HC-SR04 conversion:
     * distance_cm = echo_time_us / 58.0
     *
     * Replace with timer-capture code for the actual C8051 board.
     */
    return -1.0f;
}
