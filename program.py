import sys, os
import re
import json
import validator


def valideArgv(argv):
    if len(argv)<2:
        print("Too few arguments")
        return False
    
    if not re.search(r"\w+.json",argv[0]):
        print("Argument 1 needs to be json filename")
        return False
    
    if not re.search(r"\w+.json",argv[1]):
        print("Argument 2 needs to be json filename")
        return False

    
    return True


def parseJsonToDict(expressionFilename):
    with open(expressionFilename) as json_file:
        data = json.load(json_file)
        return data


def writeOutputToJson(outputFilename,output):
    # exist or not.
    if not os.path.isdir("output"):
        os.makedirs("output")
    with open(outputFilename, "w") as outputFile:
        json.dump(output, outputFile)

def main(argv):
    if not valideArgv(argv):
        return
    
    print("argv validated")

    sliceExpressionsList = parseJsonToDict(argv[0])
    print("slices loaded")
    vulnerabilitiesPatternsList = parseJsonToDict(argv[1])
    print("vulnerabilities patterns loaded")
    output = []
    for vulnerability in vulnerabilitiesPatternsList:
        output.append(validator.testVulnerabilityinSlice(vulnerability, sliceExpressionsList))

    writeOutputToJson("output/" + argv[0][:-5] + ".output.json",output)


if __name__ == "__main__":
    main(sys.argv[1:]) 