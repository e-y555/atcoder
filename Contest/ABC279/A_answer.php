<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}
$S = $inputs[0][0];

$count = 0;
for ($i = 0; $i < strlen($S); $i++) {
    if ($S[$i] === 'v') {
        $count += 1;
    } elseif ($S[$i] === 'w') {
        $count += 2;
    }
}
echo $count . PHP_EOL;
