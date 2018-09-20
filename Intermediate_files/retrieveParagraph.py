import json

def retrieveParagraph(jsonFilename):
    jsonDir = './data/json/'
    paragraphDir = './data/paragraph/'
    
    paragraphFilename = jsonFilename[0:-5]+'.txt'
    
    f = open(paragraphDir + paragraphFilename, 'w')
    with open(jsonDir + jsonFilename, 'r') as fp:
        for line in fp:
            obj = json.loads(line)
            textType = obj['type']
            if textType == 'paragraph':
                f.write(obj['content'])
        f.close()     