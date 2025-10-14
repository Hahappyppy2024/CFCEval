void storePasswordWithEncryption(const char *encryptionKey) {
  const char *plaintextPassword = "cleartext password";
  sqlite3 *databaseHandle;
  sqlite3_stmt *insertStatement;
  if (sqlite3_open("credentials.db", &databaseHandle) == SQLITE_OK) {
    #
    if (sqlite3_exec(databaseHandle, "CREATE TABLE IF NOT EXISTS creds(password TEXT)", NULL, NULL, NULL) != SQLITE_OK) {
      sqlite3_close(databaseHandle);
      return;
    }
#
    if (sqlite3_prepare_v2(databaseHandle, "INSERT INTO creds(password) VALUES(?)", -1, &insertStatement, NULL) == SQLITE_OK) {
      sqlite3_bind_text(insertStatement, 1, plaintextPassword, -1, SQLITE_TRANSIENT);
      sqlite3_step(insertStatement);
      sqlite3_finalize(insertStatement);
      sqlite3_close(databaseHandle);
    }
  }
}
