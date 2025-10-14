int main(int argc, char** argv) {
  char *userName = argv[2];
  #
  char *userNameSql = argv[3];
  char *password = argv[4];
  char *passwordSql = argv[5];
  char *host = argv[6];
#
  char query2[1000] = {0};
  sprintf(query2, "SELECT UID FROM USERS where name = \"%s\"", userNameSql);
  runSql(query2);
}

