from markdownify import markdownify

file = r"/Users/oesterli/Desktop/project/test/objc_LG_GeolAssets_V1.html"

file = open(file, "r").read()
html = markdownify(file, heading_style="ATX")

myMD = open("sample.md","w")
myMD.write(html)
myMD.close()

print(html)