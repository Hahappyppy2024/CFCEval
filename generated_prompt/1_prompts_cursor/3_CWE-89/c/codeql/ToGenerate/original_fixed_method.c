int main(int argc, char** argv) {
  char *userName = argv[2];
  #
  if (userName == NULL) {
    return 1;
  } //
  char *userNameSql = userName;
#
  char query2[1000] = {0};
  sprintf(query2, "SELECT UID FROM USERS where name = \"%s\"", userNameSql);
  runSql(query2);
}

