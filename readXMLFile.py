import json
import xmltodict
r=xmltodict.parse(open('.xml file location on your local').read(), process_namespaces=True)
print(json.dumps(r,indent=True))