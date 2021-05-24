import json
import re
import base64
import logging

#logging
log = logging.getLogger()
if log.handlers:
    HANDLER = log.handlers[0]
else:
    HANDLER = logging.StreamHandler()
    log.addHandler(HANDLER)
log_format = '[%(levelname)s] %(asctime)s- %(message)s (File %(pathname)s, Line %(lineno)s)'
HANDLER.setFormatter(logging.Formatter(log_format))
log.setLevel(logging.INFO)

class RequestResponseProcessor:
    def __init__(self):
        self.expectedAttri = ["text"]
        #no regex
        self.response = {'status_code': 200,'data': ""}

    def validateRequest(self, requestPayload):
        if len(requestPayload.keys()) != len(self.expectedAttri) and len(requestPayload["text"]) <= 0:
            self.response["status_code"] = 400
            log.error("Invalid response: %s", requestPayload)
            return False
        else:
            if set(self.expectedAttri) <= set(list(requestPayload.keys())):
                return True
            else:
                self.response["status_code"] = 400
                log.error("Invalid response: %s", requestPayload)
                return False

    def processRequest(self, requestPayload):
        if self.validateRequest(requestPayload):
            self.response["data"] = {}
            self.response["data"]["chars"] = str(len(requestPayload["text"]))
            txt = requestPayload["text"]
            self.response["data"]["words"] = str(len(re.split(' |\n|\t',txt)))
        return self.response


def lambda_handler(event, context):
    log.info('Request: %s', event)
    req = RequestResponseProcessor()
    res = req.processRequest(event)
    log.info('Response: %s', res)
    return res

