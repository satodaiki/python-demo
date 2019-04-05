class JsonWriter():
    JSON_OBJECT_START = "{"
    JSON_OBJECT_END = "}"
    JSON_ARRAY_START = "["
    JSON_ARRAY_END = "]"
    JSON_COMMA = ","
    JSON_COLON = ":"

    

    jsonStr = None

    def __init__(self):
        self.jsonStr = ""

    def startJsonObject():
        jsonStr = jsonStr + JSON_OBJECT_START
        
    def endJsonObject():
        jsonStr = jsonStr + JSON_OBJECT_END

    def startJsonArray():
        jsonStr = jsonStr + JSON_ARRAY_START
    
    def endJsonArray():
        jsonStr = jsonStr + JSON_ARRAY_END

    def setJsonObjectKey(key -> str):
        jsonStr = jsonStr + key + JSON_COLON

    def setJsonObjectValue(value -> str):
        jsonStr = jsonStr + value


