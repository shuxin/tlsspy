import json

from pyasn1.type import univ

from tlsspy.report.base import Report


class JSONReport(Report):
    report_type = 'json'

    def render(self, results, output):
        fd = self.open(output)
        json.dump(
            results,
            fd,
            indent=2,
            sort_keys=True,
            default=self._json_handler,
        )

    def _json_handler(self, obj):
        if hasattr(obj, 'isoformat'):
            # for datetime.* objects
            return obj.isoformat()
        elif hasattr(obj, 'seconds') and hasattr(obj, 'microseconds'):
            # for datetime.timedelta objects
            return obj.seconds + (obj.microseconds / 1000000.0)
        elif isinstance(obj, univ.ObjectIdentifier):
            return str(obj)
        elif isinstance(obj, bytearray):
            return str(obj)
        else:
            raise TypeError(
                'Object of type {0} with value {1!r} is not supported'.format(
                    type(obj),
                    obj
                )
            )

Report.register(JSONReport)
