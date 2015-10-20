## Overview

    The sqlproxyws project contains a script that exposes the sqlite database stored in example.db.

## Startup

    Before using the service, you need to fill the database in file example.db with values. As an example, run the following command:

    ```
    sqlite3 example.db < Inventorydbcreation
    ```

## Api

    The user needs to send the SQL query in the query parameter in the URL. For example:

	http://Host:8090/api/db?query=SELECT * FROM inventory LIMIT 1

    The user gets as a response an array of arrays containing the column names. For example:

       {
  "result": [
    [
      "type",
      "path",
      "fileName",
      "size",
      "status",
      "date",
      "carrier",
      "format",
      "grammar"
    ],
    [
      "inv",
      "/remote/oridatacenter/RAW_DATA/altea/2004-09/PRD.NGI.OND.INV.D040930.T104005.AMA.QFA.FTP.DATA.gz",
      "PRD.NGI.OND.INV.D040930.T104005.AMA.QFA.FTP.DATA.gz",
      327680,
      "compressed",
      "2004-09-30",
      "QF",
      "edi",
      "IFLIRR:02:1:1A"
    ],
    [
      "inv",
      "/remote/oridatacenter/RAW_DATA/altea/2004-09/PRD.NGI.OND.INV.D040929.T104002.AMA.QFA.FTP.DATA.gz",
      "PRD.NGI.OND.INV.D040929.T104002.AMA.QFA.FTP.DATA.gz",
      69366591,
      "compressed",
      "2004-09-29",
      "QF",
      "edi",
      "IFLIRR:02:1:1A"
    ]
  ]
}
