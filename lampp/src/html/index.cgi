#!/usr/bin/perl
print "Content-type: text/html\n\n";

print <<EOF;
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Perlinfo</title>
<style>
body {
    margin: 0;
    padding: 20px;
}
.wrapper {
    margin: 0 auto;
    width: 900px;
}
</style>
</head>
<body>
<div class="wrapper">
EOF

$version  = "<h1>Perlinfo</h1>";
$version .= `/usr/bin/perl -V`;
$version .= "<br><hr><h2>Modules</h2>";
$version .= `find \`perl -e 'print "@INC"'\` -name '*.pm' -print`;
$version =~ s/(^\s+)//g;
$version =~ s/([\n])/<br>/g;
print $version;

print <<EOF;
</div>
</body>
</html>
EOF
