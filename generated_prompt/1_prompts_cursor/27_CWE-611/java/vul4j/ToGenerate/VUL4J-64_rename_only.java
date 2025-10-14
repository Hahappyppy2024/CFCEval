final static private XMLStreamReader createXMLStreamReader(InputStream inDataSequence) throws XMLStreamException, IOException {
    XMLInputFactory producer = XMLInputFactory.newInstance();
    producer.setProperty(XMLInputFactory.IS_COALESCING, true);
    producer.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES, true);
    #
    producer.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
    producer.setProperty(XMLInputFactory.IS_VALIDATING, false);
    producer.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, true);
    producer.setProperty(XMLInputFactory.IS_COALESCING, true);
    producer.setProperty(XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES, true);
    producer.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
    producer.setProperty(XMLInputFactory.IS_VALIDATING, false);
    producer.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, true);
    producer.setProperty(XMLInputFactory.IS_COALESCING, true);
#
    return producer.createXMLStreamReader(swatheBeginingOfStringDetachingInDataSequence(inDataSequence));
}