from datetime import datetime
from urllib.parse import quote


def parse_timestamp(timestamp):
    """Convert an ISO 8601 timestamp into a datetime."""
    if ":" == timestamp[-3]:
        # Colon in timezone string, re-create timestamp string without colon in timezone
        timestamp = timestamp[:-3]+timestamp[-2:]
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')


def update_qs(url, params):
    """A not-very-intelligent function to glom parameters onto a query string."""
    joined_qs = '&'.join('='.join((str(k), quote(str(v))))
                         for k, v in params.items())
    separator = '&' if '?' in url else '?'
    return url + separator + joined_qs


def omit_none(dict_):
    """Removes any key from a dict that has a value of None."""
    return {k: v for k, v in dict_.items() if v is not None}
