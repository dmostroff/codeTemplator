import json
from flask import jsonify

def retrieve_to_dict( func):
    def with_respository_(*args, **kwargs):
        retval = None
        try:
            df = func( *args, **kwargs)
            j = df.to_json( orient="records", date_format="iso")
            retval = json.loads(j)
        except Exception as e:
            print( sys.exc_info()[1])
            retval = { "rc": -1, "msg": str(e), "data": sys.exc_info()[1]}
        finally:
            return jsonify(retval), 200
    return with_respository_
