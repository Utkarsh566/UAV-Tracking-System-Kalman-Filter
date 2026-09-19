#ifndef GPS_H
#define GPS_H

void GPS_Init(void);
unsigned char GPS_Parse(void);
float GPS_GetLatitude(void);
float GPS_GetLongitude(void);

#endif
