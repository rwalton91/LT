/* Get argument from command line */
val id = args(0)

/* Create connection string and get response */
val conn = s"https://jsonplaceholder.typicode.com/photos?albumId=$id"
val res = scala.io.Source.fromURL(conn).mkString

/* Parse response */
val parsed = scala.util.parsing.json.JSON.parseFull(res)

/* Cast to list of maps */
val list = parsed.get.asInstanceOf[List[Map[String,Any]]]

/* Print id and title for each map in the list */
for (map <- list) 
  println("[" + map("id").asInstanceOf[Double].toInt + "] " + map("title"))
