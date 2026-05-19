<?php
header('Content-Type: text/plain');
echo "--- PHP Environment ---\n";
echo "PHP Version: " . phpversion() . "\n";
echo "Server Software: " . $_SERVER['SERVER_SOFTWARE'] . "\n";
echo "Port: " . $_SERVER['SERVER_PORT'] . "\n\n";

echo "--- Python Check ---\n";
$python_v = shell_exec("python3 --version 2>&1");
echo "python3 --version: " . ($python_v ? trim($python_v) : "Not found") . "\n";

$python_alt_v = shell_exec("python --version 2>&1");
echo "python --version: " . ($python_alt_v ? trim($python_alt_v) : "Not found") . "\n\n";

echo "--- Pip Packages Check ---\n";
$pip_list = shell_exec("pip list 2>&1");
echo "Pip components found: " . (strpos($pip_list, 'pandas') !== false ? "YES (pandas detected)" : "NO (pandas missing)") . "\n";
echo (strpos($pip_list, 'groq') !== false ? "YES (groq detected)" : "NO (groq missing)") . "\n";

echo "\n--- System Path ---\n";
echo getenv('PATH') . "\n";
?>
