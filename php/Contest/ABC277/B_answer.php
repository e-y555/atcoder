<?php

$N = trim(fgets(STDIN));

$firstArray = ['H', 'D', 'C', 'S'];
$secondArray = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'];

$S = [];
for ($i = 0; $i < $N; $i++) {
    $s = trim(fgets(STDIN));
    if (!in_array($s[0], $firstArray, true) || !in_array($s[1], $secondArray, true)) {
        echo 'No' . PHP_EOL;
        exit;
    }
    $S[] = $s;
}

if (count($S) === count(array_unique($S))) echo 'Yes' . PHP_EOL;
else echo 'No' . PHP_EOL;
