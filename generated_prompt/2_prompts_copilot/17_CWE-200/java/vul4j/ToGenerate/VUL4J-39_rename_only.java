@Override
public String toString() {
    StringBuilder s = new StringBuilder();
    if (source != null) {
        s.append("remoteAddress=").append(source);
    }
    if (customerIdentification != null) {
        if (s.length() > 0) {
            s.append(", ");
        }
        s.append("clientId=").append(customerIdentification);
    }
    #
    s.append("}");
    return s.toString();
#
}