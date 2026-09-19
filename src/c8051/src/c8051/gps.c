#include "gps.h"

static float current_latitude = 0.0f;
static float current_longitude = 0.0f;

void GPS_Init(void)
{
    current_latitude = 0.0f;
    current_longitude = 0.0f;
}

unsigned char GPS_Parse(void)
{
    /*
     * Hardware-specific implementation should:
     * 1. Read NMEA characters from UART.
     * 2. Detect GGA/RMC sentences.
     * 3. Parse latitude/longitude.
     * 4. Validate the NMEA checksum.
     */
    return 0;
}

float GPS_GetLatitude(void)
{
    return current_latitude;
}

float GPS_GetLongitude(void)
{
    return current_longitude;
}
