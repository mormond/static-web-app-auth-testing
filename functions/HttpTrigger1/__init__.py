import logging
import mimetypes

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"{{ \"text\": {name} }}",
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "{ \"text\": \"Hello.\" }",
            mimetype="application/json",
            status_code=200
        )
