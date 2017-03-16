
use warnings;
use CGI qw(:standard);
use DBI;
use CGI::Carp qw(fatalsToBrowser);
use strict;
use JSON; 
binmode STDOUT, ":utf8";
use utf8;


my @output;


my $driver = "SQLite";
my $database = "/home/www/cgi-bin/mydata.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {RaiseError=> 1}) or die $DBI::errstr;

my $sth = $dbh->prepare('select * from appointed'); 
$sth -> execute;

while(my $row = $sth->fetchrow_hashref) {
	push @output, $row;

}


my $cgi = CGI->new;
print $cgi->header('text/html');
print to_json({data=> \@output});
my $fh;
open  $fh, ">", "data_out.json";
print $fh to_json({data=> \@output});
close $fh; 
