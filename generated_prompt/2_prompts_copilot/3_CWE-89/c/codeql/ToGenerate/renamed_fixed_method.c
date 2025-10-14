int handleUserQuery(int argc, char** argv) {
    char *inputUserName = argv[2];
    #
    char escapedUserName[100];
    escapeSqlString(inputUserName, escapedUserName, sizeof(escapedUserName));
#
    char sqlQuery[1000] = {0};
    sprintf(sqlQuery, "SELECT UID FROM USERS WHERE name = \"%s\"", escapedUserName);
    runSql(sqlQuery);
}
