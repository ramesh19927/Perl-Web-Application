use warnings; 
use CGI qw(:standard);
use DBI;
use CGI::Carp qw(fatalsToBrowser);
use strict;
use HTML::Parser;

my $cgi = new CGI; 
print $cgi->header;
print $cgi->start_html(-title=>'Appointed Output');
my $dateset = param('dateset');
my $timeset = param('timeset');
my $descset = param('descset'); 

print "Date: $dateset | Time: $timeset | Description: $descset has been added to the database";
my $driver = "SQLite";
my $database = "/home/www/cgi-bin/mydata.db"; 
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {RaiseError=> 1}) or die $DBI::errstr;
my $stmt = q/INSERT INTO appointed (dateval,timeval,descval) VALUES (?,?,?)/; #the '?,?,?' is a neat way to pass values when you execute the SQL statement.
my $sth = $dbh->prepare($stmt); 
$sth->execute($dateset, $timeset, $descset);

print '<meta http-equiv="refresh" content="1;url=http://localhost/appoint.html">';

$dbh->disconnect(); 

