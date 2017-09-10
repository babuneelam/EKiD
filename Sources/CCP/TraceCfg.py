import os

enum
TraceID
{
WORKSHEET=0,
DRAW_WORD
GET_PIC
}

define array


enum
TraceLevel
{
INFO=0,
WARN,
ERROR
CRITICAL
}


class TraceFilters:
    TraceLevel = 'Error'

    @classmethod
    def __init__(cls, trace_file):
        # Initialize all trace filters to error level

        # Parse filter file for configured filters
        filters_file = open(trace_file)
        filters = filters_file.readlines()

        for filter in filters:
            filter = filter.rstrip()
            # Extract TraceLevel and TraceType(optional)

            if filter == 'AnyLicense':
                cls.License = 'AnyLicense'
            elif filter == 'FreeLicense':
                cls.Liense = 'FreeLicense'
            elif filter == 'AllImages':
                cls.ImageType = 'AllImages'
            elif filter == 'LineartImages':
                cls.ImageType = 'LineartImages'
            else:
               continue
    def TRACE(self, traceID, traceMsg, ....)
        pass
 

