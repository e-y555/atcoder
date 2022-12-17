<?php

[$N, $Q] = explode(' ', trim(fgets(STDIN)));

$user = [];
$op = [];
for ($i = 0; $i < $Q; $i++) {
    $op =  explode(' ', trim(fgets(STDIN)));
    if ($op[0] == 1) {
        $user[$op[1]][$op[2]] = 1;
    } elseif ($op[0] == 2) {
        $user[$op[1]][$op[2]] = 0;
    } elseif ($op[0] == 3) {
        $check1 = isset($user[$op[1]][$op[2]]) && $user[$op[1]][$op[2]] === 1;
        $check2 = isset($user[$op[2]][$op[1]]) && $user[$op[2]][$op[1]] === 1;
        if ($check1 && $check2) {
            echo 'Yes' . PHP_EOL;
        } else {
            echo 'No' . PHP_EOL;
        }
    }
}
