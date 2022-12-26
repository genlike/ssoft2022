def testVulnerabilityinSlice(vulnerability, expressionsSlice):
    print("Testing")
    print(vulnerability)
    print("Slice")
    print(expressionsSlice)
    return buildVulnerability(vulnerability["vulnerability"], "", "", [], "")


def buildVulnerability(vulnerability, source, sink, unsanitized_flows, sanitized_flows):
    return {
        "vulnerability": vulnerability,
        "source": source,
        "sink": sink,
        "unsanitized_flows": unsanitized_flows,
        "sanitized_flows": sanitized_flows,
    }