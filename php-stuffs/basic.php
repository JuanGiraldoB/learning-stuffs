<?php
    $name = "miguel";
    $isDev = false;
    $age = 0;
    $output = "Hola $name, con una edad de  $age";
    
    $isOld = $age > 40;
    $outputAge = match(true) {
        $age < 2 => "bebe, $name",
        $age < 10 => "adolescente, $name",
        default => "cucho",
    };

    $bestLanguages = ["php", "js", "python"];
    $bestLanguages[] = 'java';
    $bestLanguages[] = 'ts';

    $person = [
        "name" => "miguel",
        "age" => 80,
        "isDev" => true,
        "lannguages" => ["php", "js", "python"],
    ];

    $person["name"] = "juan";
    $person["languages"][] = "java";

    if ($isOld){
        echo "<h2>Viejo</h2>";
    } elseif ($isDev){
        echo "eres dev";
    } else {
        echo "<h2>Joven</h2>";
    }

    // Constante global
    define('LOGO_URL', "x");

    // Constante local
    const NOMBRE = 'Juan';

?>

<ul>
    <?php foreach($bestLanguages as $key => $language) : ?>
        <li><?= $key . " " . $language ?></li>
    <?php endforeach; ?>
</ul>

<?php if ($isOld) : ?>
    <h2>Viejo</h2>
<?php elseif ($isDev) : ?>
    <h2>Dev</h2>
<?php else : ?>
    <h2>Joven</h2>
<?php endif; ?>


<h1>
    <?=
    $bestLanguages[4]
    ?>
</h1>

<style>
    :root {
        color-scheme: light dark;
    }

    body {
        display: grid;
        place-content: center;
    }
</style>