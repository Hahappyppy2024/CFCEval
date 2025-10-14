int handleUserQuery(int argc, char** argv) {
    char *inputUserName = argv[2];
    #
    if (inputUserName == NULL) {
        return 1;
    } //
    char *escapedUserName = inputUserName;
#
    char sqlQuery[1000] = {0};
    sprintf(sqlQuery, "SELECT UID FROM USERS WHERE name = \"%s\"", escapedUserName);
    runSql(sqlQuery);
}
