/*
 * UAV Tracking System with Kalman Filter & Obstacle Detection
 * Reconstructed educational C8051 prototype.
 *
 * Adapt UART, timer, GPIO and clock settings to the exact C8051
 * derivative and development board being used.
 */
#include <C8051Fxxx.h>
#include "gps.h"
#include "ultrasonic.h"

#define SYSCLK 24500000UL
#define OBSTACLE_THRESHOLD_CM 100

volatile unsigned char obstacle_detected = 0;
float latitude = 0.0f;
float longitude = 0.0f;
float obstacle_distance_cm = -1.0f;

void SYSCLK_Init(void);
void PORT_Init(void);
void UART0_Init(void);
void Timer0_Init(void);
void delay_ms(unsigned int ms);

void main(void)
{
    SYSCLK_Init();
    PORT_Init();
    UART0_Init();
    Timer0_Init();

    GPS_Init();
    Ultrasonic_Init();

    EA = 1;

    while (1)
    {
        if (GPS_Parse())
        {
            latitude = GPS_GetLatitude();
            longitude = GPS_GetLongitude();
        }

        obstacle_distance_cm = Ultrasonic_ReadDistanceCm();

        if (obstacle_distance_cm > 0 &&
            obstacle_distance_cm <= OBSTACLE_THRESHOLD_CM)
            obstacle_detected = 1;
        else
            obstacle_detected = 0;

        /* Telemetry can transmit:
           timestamp, latitude, longitude, distance_cm */
        delay_ms(100);
    }
}

void SYSCLK_Init(void)
{
    /* Configure clock for the selected C8051 derivative. */
}

void PORT_Init(void)
{
    /* Configure GPIO according to the actual board wiring. */
}

void UART0_Init(void)
{
    /* Configure UART0 for GPS/telemetry. */
}

void Timer0_Init(void)
{
    /* Configure Timer0 for delays/ultrasonic timing. */
}

void delay_ms(unsigned int ms)
{
    volatile unsigned int i;
    while (ms--)
        for (i = 0; i < 1000; i++);
}
