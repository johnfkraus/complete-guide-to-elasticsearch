# source: https://www.epochconverter.com/
import calendar, time

ES_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

# date_string = '2000-01-01 12:34:00'
# format = '%Y-%m-%d %H:%M:%S%z'
# epoch = calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))

def make_query_snippet(es_date_string, epoch_ms):
    frag = f"""
    "created": {epoch_ms},
    "expires": "{es_date_string}"
    """
    print(frag)
    return frag
    # frag = f'"created": {epoch_ms},
    #     "expires": {es_date_string}
    #     }'
    # print(frag)
    # return frag


def es_date_string_to_epoch_ms(es_date_string):
    epoch = calendar.timegm(time.strptime(es_date_string, ES_DATE_FORMAT))
    epoch_ms = epoch * 1000
    result_string = f"{es_date_string=} >> {epoch_ms=}"
    print(result_string)
    # print(f"{epoch_ms=}\n")
    return epoch_ms

def main():
    es_date_strings = ['2025-04-15T13:07:41Z', '2015-01-01T01:00:21Z',
        "2007-04-15T13:07:41Z"]
    for date_string in es_date_strings:
        epoch_ms = es_date_string_to_epoch_ms(date_string)
        make_query_snippet(date_string, epoch_ms)

if __name__ == "__main__":
    main()

# 
# 
# print(es_date_string_to_epoch_ms('2015-01-01T01:00:21Z'))
# 

# es_date_string = '2025-04-15T13:07:41Z'
# es_date_format = '%Y-%m-%dT%H:%M:%S%z'
# epoch = calendar.timegm(time.strptime(es_date_string, es_date_format))
# print(f"{es_date_string}")
# # print(f"{epoch=}")
# epoch_ms = epoch * 1000
# print(f"{epoch_ms=}")
#
#
# es_date_string = '2015-04-15T13:07:41Z'
# es_date_format = '%Y-%m-%dT%H:%M:%S%z'
# epoch = calendar.timegm(time.strptime(es_date_string, es_date_format))
# print(f"{es_date_string}")
# # print(f"{epoch=}")
# epoch_ms = epoch * 1000
# print(f"{epoch_ms=}")
#
# es_date_format = '%Y-%m-%dT%H:%M:%S%z'