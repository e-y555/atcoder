<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}

$S = $inputs[0][0];
$T = $inputs[1][0];

$r = 0;
for ($i = 0; $i < strlen($T); $i++) {
    if ($S[$i] === $T[$i]) {
        continue;
    } else {
        echo $i + 1 . PHP_EOL;
        break;
    }
    echo $i + 1 . PHP_EOL;
}
