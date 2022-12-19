<?php

[$N, $X] = explode(' ', trim(fgets(STDIN)));
$P = array_map('intval', explode(' ', trim(fgets(STDIN))));

for ($i = 0; $i < $N; $i++) {
    if ($P[$i] == $X) echo $i + 1 . PHP_EOL;
}
