from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

def durationfunc(file):
 metadata = extractMetadata(createParser(f"""{file}"""))
 if metadata.has("duration"):
   duration = metadata.get('duration').seconds
 else:
     duration = 10
 return duration
