#https://github.com/OpenRefine/OpenRefine/commit/6a0d7d56e4ffb420316ce7849fde881344fbf881
final static private XMLStreamReader createXMLStreamReader(InputStream inputStream) throws XMLStreamException, IOException {
    XMLInputFactory factory = XMLInputFactory.newInstance();
    factory.setProperty(XMLInputFactory.IS_COALESCING, true);
    factory.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES, true);
    return factory.createXMLStreamReader(wrapPrefixRemovingInputStream(inputStream));
}
