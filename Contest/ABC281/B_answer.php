<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}

$input = $inputs[0][0];

if (strlen($input) !== 8) {
    echo 'No';
    return;
}

$a = $input[0];
$b = $input[7];
$c = substr($input, 1, 6);

if (!ctype_alpha($a) || !ctype_upper($a)) {
    echo 'No';
    return;
}
if (!ctype_alpha($b) || !ctype_upper($b)) {
    echo 'No';
    return;
}

if (!ctype_digit($c) || $c < 100000 || $c > 999999) {
    echo 'No';
    return;
}
echo 'Yes';
