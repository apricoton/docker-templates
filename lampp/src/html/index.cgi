#!/usr/bin/perl
print "Content-type: text/html\n\n";

print <<EOF;
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>バージョン</title>
</head>
<body>
EOF

$version  = `/usr/bin/perl -V`;
$version .= "<br><hr><h2>Modules</h2>";
$version .= `find \`perl -e 'print "@INC"'\` -name '*.pm' -print`;
$version =~ s/(^\s+)//g;
$version =~ s/([\n])/<br>/g;
print $version;

print <<EOF;
</body>
</html>
EOF
