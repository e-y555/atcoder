<?php

$inputs = [];
while ($input = trim((string) fgets(STDIN))) {
    $inputs[] = explode(' ', $input);
}

$input = $inputs[0][0];
for ($i = 0; $i <= $input; $i++) {
    echo $input - $i . "\n";
}
