int handleUserQuery(int argc, char** argv) {
    char *inputUserName = argv[2];

    // GOOD: Escape SQL injection characters
    char escapedUserName[1000] = {0};
    encodeSqlString(escapedUserName, 1000, inputUserName);

    char sqlQuery[1000] = {0};
    sprintf(sqlQuery, "SELECT UID FROM USERS WHERE name = \"%s\"", escapedUserName);

    runSql(sqlQuery);
}
