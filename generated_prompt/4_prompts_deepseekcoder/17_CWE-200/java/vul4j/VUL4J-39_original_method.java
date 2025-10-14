#https://github.com/cloudfoundry/uaa/commit/a61bfabbad22f646ecf1f00016b448b26a60daf#diff-7f92051ccc7d95d8559a929bb820949ef8fe7902a6ee3803c55c7596cff03d12R16-L116
@Override
public String toString() {
    StringBuilder sb = new StringBuilder();
    if (origin != null) {
        sb.append("remoteAddress=").append(origin);
    }
    if (clientId != null) {
        if (sb.length() > 0) {
            sb.append(", ");
        }
        sb.append("clientId=").append(clientId);
    }
    if (sessionId != null) {
        if (sb.length() > 0) {
            sb.append(", ");
        }
        sb.append("sessionId=").append(sessionId);
    }
    return sb.toString();
}
