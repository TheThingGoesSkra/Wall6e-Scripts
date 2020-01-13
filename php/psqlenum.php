<?php 

$host = "127.0.0.1"; 
$user = "gitlab"; 
$pass = "gitlab"; 
$db = "gitlab"; 

$con = pg_connect("host=$host dbname=$db user=$user password=$pass")
    or die ("Could not connect to server\n"); 

$query = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'"; 

$rs = pg_query($con, $query) or die("Cannot execute query: $query\n");

while ($row = pg_fetch_row($rs)) {
  echo "$row[0] $row[1]\n";
}

pg_close($con); 

?>

